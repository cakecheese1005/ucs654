import sys
import os
from youtube_search import YoutubeSearch
import yt_dlp
# FIXED IMPORT FOR MOVIEPY 2.0:
from moviepy import AudioFileClip, concatenate_audioclips

def download_and_process(singer, n, duration, output_file):
    # 1. Search for Videos
    print(f"Searching for {n} videos of {singer}...")
    try:
        results = YoutubeSearch(singer, max_results=n+5).to_dict()
    except Exception as e:
        print(f"Error searching: {e}")
        return

    # 2. Setup Options for Downloading
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'temp/%(id)s.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    # 3. Download
    urls = []
    for v in results:
        urls.append(f"https://www.youtube.com/watch?v={v['id']}")
    
    print("Downloading audio... (this may take time)")
    if not os.path.exists('temp'):
        os.makedirs('temp')

    count = 0
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            if count >= n:
                break
            try:
                ydl.download([url])
                count += 1
            except:
                continue

    # 4. Cut and Merge using MoviePy
    print("Processing audio files...")
    clips = []
    
    files = [f for f in os.listdir('temp') if f.endswith('.mp3')]
    files = files[:n]

    for file in files:
        file_path = os.path.join('temp', file)
        try:
            # Load the audio file
            audio = AudioFileClip(file_path)
            # Cut the first 'duration' seconds
            # We use min() to ensure we don't crash if the audio is shorter than the duration
            cut_audio = audio.subclipped(0, min(duration, audio.duration))
            clips.append(cut_audio)
        except Exception as e:
            print(f"Skipping a file due to error: {e}")

    if len(clips) > 0:
        print("Merging files...")
        final_audio = concatenate_audioclips(clips)
        final_audio.write_audiofile(output_file, codec='libmp3lame')
        print(f"Done! Saved as {output_file}")
        
        # Close clips to release files so we can delete them
        final_audio.close()
        for clip in clips:
            clip.close()
    else:
        print("Error: No audio clips were processed successfully.")

    # Cleanup
    try:
        for file in os.listdir('temp'):
            os.remove(os.path.join('temp', file))
        os.rmdir('temp')
    except:
        pass

def main():
    if len(sys.argv) != 5:
        print("Usage: python 102483081.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer_name = sys.argv[1]
    try:
        num_videos = int(sys.argv[2])
        audio_duration = int(sys.argv[3])
    except ValueError:
        print("Error: NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_filename = sys.argv[4]
    
    if not output_filename.endswith('.mp3'):
        output_filename += '.mp3'

    download_and_process(singer_name, num_videos, audio_duration, output_filename)

if __name__ == "__main__":
    main()
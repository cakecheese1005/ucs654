from flask import Flask, request, send_file
import os
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from youtube_search import YoutubeSearch
import yt_dlp
# FIXED IMPORT FOR MOVIEPY 2.0
from moviepy import AudioFileClip, concatenate_audioclips

app = Flask(__name__)

# --- 1. MASHUP LOGIC (Same as your script) ---
def create_mashup(singer, n, duration, output_file):
    try:
        results = YoutubeSearch(singer, max_results=n+5).to_dict()
        urls = [f"https://www.youtube.com/watch?v={v['id']}" for v in results]
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}],
            'outtmpl': 'temp_web/%(id)s.%(ext)s',
            'quiet': True,
            'noplaylist': True
        }

        if not os.path.exists('temp_web'): os.makedirs('temp_web')

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            count = 0
            for url in urls:
                if count >= n: break
                try: 
                    ydl.download([url])
                    count += 1
                except: continue

        clips = []
        files = [f for f in os.listdir('temp_web') if f.endswith('.mp3')][:n]
        
        for f in files:
            try:
                path = os.path.join('temp_web', f)
                audio = AudioFileClip(path)
                cut = audio.subclipped(0, min(duration, audio.duration))
                clips.append(cut)
            except: pass
            
        if clips:
            final = concatenate_audioclips(clips)
            final.write_audiofile(output_file, codec='libmp3lame')
            final.close()
            for c in clips: c.close()

        # Cleanup
        for f in os.listdir('temp_web'):
            try: os.remove(os.path.join('temp_web', f))
            except: pass
        try: os.rmdir('temp_web')
        except: pass
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# --- 2. EMAIL LOGIC ---
def send_email(user_email, filename):
    # !!! IMPORTANT: PUT YOUR DETAILS HERE !!!
    my_email = "sandeepkaur1952004@gmail.com"        # <--- CHANGE THIS
    my_password = "cxct toxw aaau nxic"        # <--- CHANGE THIS (16 chars)

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = user_email
    msg['Subject'] = "Your Mashup Result"

    with open(filename, "rb") as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_email, my_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        return False

# --- 3. WEB PAGES ---
@app.route('/')
def home():
    return '''
    <html>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h2>Mashup Generator</h2>
            <form action="/mashup" method="post">
                <label>Singer Name:</label><br>
                <input type="text" name="singer" required><br><br>
                
                <label>Number of Videos (>10):</label><br>
                <input type="number" name="count" min="11" required><br><br>
                
                <label>Duration (sec) (>20):</label><br>
                <input type="number" name="duration" min="21" required><br><br>
                
                <label>Email Id:</label><br>
                <input type="email" name="email" required><br><br>
                
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    '''

@app.route('/mashup', methods=['POST'])
def process():
    singer = request.form['singer']
    count = int(request.form['count'])
    duration = int(request.form['duration'])
    email = request.form['email']
    
    mp3_file = "mashup_result.mp3"
    zip_file = "mashup_result.zip"
    
    # Run Logic
    success = create_mashup(singer, count, duration, mp3_file)
    
    if success:
        # Zip it
        with zipfile.ZipFile(zip_file, 'w') as z:
            z.write(mp3_file)
        
        # Email it
        email_success = send_email(email, zip_file)
        
        if email_success:
            return f"<h2>Success! Sent mashup of {singer} to {email}</h2>"
        else:
            return "<h2>Mashup created, but Email failed. Check console for error.</h2>"
    else:
        return "<h2>Failed to create mashup.</h2>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
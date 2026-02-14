# Mashup Generator Assignment

Roll Number: 102303594
Program: Mashup Generator (Python)

---

## Project Description

This project implements a command-line tool and a web service to create a "mashup" of audio from YouTube videos. It downloads multiple videos of a specified singer, extracts the audio, cuts them to a specific duration, and merges them into a single MP3 file.

---

## Methodology

The assignment is solved in two parts:

### Part 1: CLI Script (102483081.py)

**Input:**  
The script accepts command-line arguments: Singer Name, Number of Videos, Duration, and Output Filename.

**Search:**  
Uses Youtube-python to find video URLs for the given singer.

**Download:**  
Uses yt-dlp to download the audio streams from YouTube.

**Processing:**  
- Iterates through downloaded files using moviepy.  
- Trims each audio file to the specified duration (e.g., 20 seconds).  
- Concatenates all clips into a single audio track.

**Output:**  
Exports the final mix as an MP3 file.

---

### Part 2: Web Service (app.py)

**Framework:**  
Uses Flask to create a web interface.

**User Interface:**  
A HTML form allows users to input parameters (Singer, Count, Duration, Email).

**Backend Logic:**  
Reuses the logic from Part 1 to generate the mashup on the server.

**Email Delivery:**  
- The generated MP3 is compressed into a ZIP file.  
- Uses Python's smtplib to email the ZIP file to the user's provided email address.

---

## How to Run

### Install Prerequisites

pip install yt-dlp moviepy youtube-search-python flask


(Ensure FFmpeg is installed and added to PATH).

---

### Run CLI Script

python 102303594.py "Singer Name" 10 20 output.mp3

##Run web app
Access at:http://127.0.0.1:5000/

---

## Libraries Used

- yt-dlp: For downloading YouTube content.
- moviepy: For audio processing (cutting/merging).
- flask: For the web server.
- smtplib: For sending emails.

---


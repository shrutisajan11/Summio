'''from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Read the transcript from the file
    video_id = "AwhBTrzzqeg"  # Replace with the actual video ID
    transcript_file_path = f"youtube_transcripts/{video_id}_transcript.txt"
    
    try:
        with open(transcript_file_path, "r", encoding="utf-8") as file:
            transcript_content = file.read()
    except FileNotFoundError:
        transcript_content = "Transcript not found."

    return render_template('index.html', transcript=transcript_content)


if __name__ == '__main__':
    app.run(debug=True,port=5000, host='127.0.0.1')'''
   # app.py
# app.py

from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import os
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    transcript = None

    if request.method == 'POST':
        # Get YouTube video URL from the form
        video_url = request.form['youtube_url']

        # Extract video ID using urllib.parse
        video_id = urllib.parse.urlparse(video_url).query.split('=')[-1]

        # Fetch YouTube transcript
        transcript = get_youtube_transcript(video_id)

        if transcript is None:
            error_message = "Transcript not found. Please check the video URL and try again."

    return render_template('index.html', transcript=transcript, error_message=error_message)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/help')
def help():
    return render_template('help.html')

def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return "\n".join(entry['text'] for entry in transcript)
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')

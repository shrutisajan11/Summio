from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html', transcripts={}, error_messages={})

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/get_youtube_transcript', methods=['POST'])
def get_youtube_transcript():
    transcripts = {}
    error_messages = {}

    if request.method == 'POST':
        # Get YouTube video URLs from the form
        video_urls = request.form.getlist('youtube_url')

        for url in video_urls:
            # Extract video ID using urllib.parse
            video_id = urllib.parse.urlparse(url).query.split('=')[-1]
            try:
                # Fetch YouTube transcript
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
                # Join transcript entries into a single string
                transcripts[url] = "\n".join(entry['text'] for entry in transcript)
            except Exception as e:
                print(f"Error fetching transcript for {url}: {e}")
                error_messages[url] = "Transcript not found. Please check the video URL and try again."

    return render_template('index.html', transcripts=transcripts, error_messages=error_messages)

if __name__ == '__main__':
    app.run(debug=True)

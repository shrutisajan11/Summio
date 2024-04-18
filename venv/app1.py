from flask import Flask, render_template, request
from flask import redirect, url_for
import urllib.parse
from youtube_transcript_api import YouTubeTranscriptApi
import spacy

app = Flask(__name__, template_folder='templates', static_folder='static')

# Load the English language model provided by spaCy
nlp = spacy.load('en_core_web_sm')

@app.route('/')
def index():
    error_message = None
    transcript = None
    return render_template('index.html', transcript=transcript, error_message=error_message)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/static')
def redirect_to_html():
    return summary(url_for('static'))

@app.route('/get_youtube_transcript', methods=['POST'])
def get_youtube_transcript():
    error_message = None
    transcript = None

    if request.method == 'POST':
        # Get YouTube video URL from the form
        video_url = request.form['youtube_url']

        # Extract video ID using urllib.parse
        video_id = urllib.parse.urlparse(video_url).query.split('=')[-1]

        try:
            # Fetch YouTube transcript
            transcript_entries = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

            # Join transcript entries into a single string
            transcript = "\n".join(entry['text'] for entry in transcript_entries)
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            error_message = "Transcript not found. Please check the video URL and try again."

    return render_template('index.html', transcript=transcript, error_message=error_message)


'''@app.route('/summaryy')
def summary(video_url):
    error_message = None
    transcript = None
    try:
        # Extract video ID from URL
        video_id = urllib.parse.urlparse(video_url).query.split('=')[-1]

        # Fetch YouTube transcript
        transcript_entries = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        # Join transcript entries into a single string
        transcript = "\n".join(entry['text'] for entry in transcript_entries)

        # Process the transcript using spaCy
        doc = nlp(transcript)

        # Extract sentences and calculate their scores
        sentence_scores = {sentence.text: sentence.similarity(doc) for sentence in doc.sents}

        # Get the top N sentences with highest scores
        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]

        # Join the top sentences to form the summary
        summary = ' '.join(top_sentences)

        return summary

    except Exception as e:
        print(f"Error fetching transcript or summarizing: {e}")
        error_message = "Transcript not found. Please check the video URL and try again."
        return None
    return render_template('summaryy.html', transcript=transcript, error_message=error_message)'''
    

@app.route('/summaryy.html/<path:video_url>')
def summary(video_url):
    error_message = None
    transcript = None
    summary = None
    try:
        # Extract video ID from URL
        video_id = urllib.parse.urlparse(video_url).query.split('=')[-1]

        # Fetch YouTube transcript
        transcript_entries = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        # Join transcript entries into a single string
        transcript = "\n".join(entry['text'] for entry in transcript_entries)
        transcripts = {video_url: transcript}

        # Process the transcript using spaCy
        doc = nlp(transcript)

        # Extract sentences and calculate their scores
        sentence_scores = {sentence.text: sentence.similarity(doc) for sentence in doc.sents}

        # Get the top N sentences with highest scores
        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]

        # Join the top sentences to form the summary
        summary = ' '.join(top_sentences)

    except Exception as e:
        print(f"Error fetching transcript or summarizing: {e}")
        error_message = "Transcript not found. Please check the video URL and try again."

    return render_template('summaryy.html', transcript=transcript, summary=summary, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)

    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


    shummary = summary(video_url)

    # Print the summary if successful
    if shummary:
        print("Summary:")
        print(shummary)
    else:
        print("Error: Could not summarize the video.")

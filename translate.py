from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
#from gensim.summarization import summarize
from mtranslate import translate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    summary = None
    translated_summaries = None

    if request.method == 'POST':
        # Get YouTube video URL from the form
        video_url = request.form['youtube_url']

        # Extract video ID using urllib.parse
        video_id = video_url.split('v=')[-1]

        # Fetch YouTube transcript
        transcript = get_youtube_transcript(video_id)

        if transcript:
            # Summarize the transcript using gensim
            #summary = summarize_transcript(transcript)

            # Translate the summary to multiple languages
            target_languages = ['fr', 'es', 'de']  # Add your desired language codes to the list
            translated_summaries = translate_summary(summary, target_languages)
        else:
            error_message = "Transcript not found. Please check the video URL and try again."

    return render_template('index.html', summary=summary, translated_summaries=translated_summaries, error_message=error_message)

def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return "\n".join(entry['text'] for entry in transcript)
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def summarize_transcript(transcript):
    # Summarize the transcript using gensim's summarize function
    summary = summarize(transcript, ratio=0.2)  # You can adjust the 'ratio' parameter for desired summary length
    return summary

def translate_summary(summary, target_languages):
    # Translate the summary to multiple target languages using the mtranslate library
    translated_summaries = {}

    for dest_language in target_languages:
        translation = translate(summary, dest=dest_language)
        translated_summaries[dest_language] = translation

    return translated_summaries

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')

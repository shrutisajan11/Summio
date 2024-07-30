from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import mtranslate

app = Flask(__name__, template_folder='templates', static_folder='static')

# Download the necessary resources for NLTK
nltk.download('stopwords')
nltk.download('punkt')

@app.route('/')
def index():
    return render_template('index.html', transcripts={}, error_messages={})

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/summaryy')
def summaryy():
    return render_template('summaryy.html')

@app.route('/translate')
def translate():
    return render_template('translate.html')

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

@app.route('/get_summary_transcript', methods=['POST'])
def get_summary_transcript():
    try:
        # Extract video ID from request
        video_id = request.json.get('video_id')
        
        # Fetch YouTube transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        
        # Extract text from transcript
        text = "\n".join(entry['text'] for entry in transcript)
        
        # Tokenize the text
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        
        # Calculate frequency distribution of words
        freq_dist = FreqDist(filtered_tokens)
        
        # Get 10 most common words
        most_common_words = freq_dist.most_common(10)
        
        # Extract sentences containing most common words
        summary_sentences = []
        for entry in transcript:
            sentence = entry['text']
            if any(word in sentence.lower() for word, _ in most_common_words):
                summary_sentences.append(sentence)
        
        # Combine summary sentences into a single string
        summary_text = "\n".join(summary_sentences)
        
        # Translate summary to Spanish and Italian
        spanish_summary = mtranslate.translate(summary_text, 'es')
        italian_summary = mtranslate.translate(summary_text, 'it')
        
        # Return summary and translated summaries as JSON response
        return jsonify({
            'summary': summary_text,
            'spanish_summary': spanish_summary,
            'italian_summary': italian_summary
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import mtranslate

app = Flask(__name__, template_folder='templates', static_folder='static')

# Download the necessary resources for NLTK
nltk.download('stopwords')
nltk.download('punkt')

@app.route('/')
def index():
    return render_template('index.html', transcripts={}, error_messages={})

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/summaryy')
def summaryy():
    return render_template('summaryy.html')

@app.route('/translate')
def translate():
    return render_template('translate.html')

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

@app.route('/get_summary_transcript', methods=['POST'])
def get_summary_transcript():
    try:
        # Extract video ID from request
        video_id = request.json.get('video_id')
        
        # Fetch YouTube transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        
        # Extract text from transcript
        text = "\n".join(entry['text'] for entry in transcript)
        
        # Tokenize the text
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        
        # Calculate frequency distribution of words
        freq_dist = FreqDist(filtered_tokens)
        
        # Get 10 most common words
        most_common_words = freq_dist.most_common(10)
        
        # Extract sentences containing most common words
        summary_sentences = []
        for entry in transcript:
            sentence = entry['text']
            if any(word in sentence.lower() for word, _ in most_common_words):
                summary_sentences.append(sentence)
        
        # Combine summary sentences into a single string
        summary_text = "\n".join(summary_sentences)
        
        # Translate summary to Spanish and Italian
        spanish_summary = mtranslate.translate(summary_text, 'es')
        italian_summary = mtranslate.translate(summary_text, 'it')
        
        # Return summary and translated summaries as JSON response
        return jsonify({
            'summary': summary_text,
            'spanish_summary': spanish_summary,
            'italian_summary': italian_summary
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



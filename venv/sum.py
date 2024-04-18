 from youtube_transcript_api import YouTubeTranscriptApi
from gensim import summarize
import os
import urllib.parse

def get_youtube_transcript(video_url):
    try:
        # Extract video ID using urllib.parse
        video_id = urllib.parse.urlparse(video_url).path.split('/')[-1]

        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en','ml'])

        # Create a directory to save the transcript
        output_dir = "youtube_transcripts"
        os.makedirs(output_dir, exist_ok=True)

        # Save the transcript to a text file
        output_file = os.path.join(output_dir, f"{video_id}_transcript.txt")
        with open(output_file, "w", encoding="utf-8") as file:
            for entry in transcript:
                file.write(f"{entry['text']}\n")

        print(f"Transcript saved to: {output_file}")
        
        # Summarize the transcript
        summarized_transcript = summarize(' '.join(entry['text'] for entry in transcript), ratio=0.2)

        return summarized_transcript

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    summarized_transcript = get_youtube_transcript(video_url)
    if summarized_transcript:
        print("Summarized transcript:")
        print(summarized_transcript)
    else:
        print("Failed to summarize the transcript.")

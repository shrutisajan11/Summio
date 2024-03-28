from youtube_transcript_api import YouTubeTranscriptApi
from gensim.summarization import summarize

# Define function to summarize YouTube video
def summarize_youtube_video(video_url):
  """
  This function fetches the transcript of a YouTube video and summarizes it using Gensim.

  Args:
      video_url: The URL of the YouTube video.

  Returns:
      A string containing the summarized transcript.
  """
  try:
    # Extract video ID from URL
    video_id = urllib.parse.urlparse(video_url).query.split('=')[-1]

    # Fetch YouTube transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

    # Join transcript entries into a single string
    transcript = "\n".join(entry['text'] for entry in transcript)

    # Summarize the transcript using Gensim
    summary = summarize(transcript, ratio=0.2)  # Adjust ratio for desired summary length

    return summary

  except Exception as e:
    print(f"Error fetching transcript or summarizing: {e}")
    return None

# Example usage
if __name__ == "__main__":
  # Replace with the actual YouTube video URL
  video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

  # Get the summary
  summary = summarize_youtube_video(video_url)

  # Print the summary if successful
  if summary:
    print("Summary:")
    print(summary)
  else:
    print("Error: Could not summarize the video.")

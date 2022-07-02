from youtube_transcript_api import YouTubeTranscriptApi
  
# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("3inFWGBsrKc&t=193s", languages=['en'])

print(srt)
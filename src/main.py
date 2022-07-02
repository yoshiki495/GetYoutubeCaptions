from flask import Flask, render_template, url_for, request, redirect
from youtube_transcript_api import YouTubeTranscriptApi
  
app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    # assigning srt variable with the list
    # of dictonaries obtained by the get_transcript() function
    youtube_id = request.args.get('id')
    srt = YouTubeTranscriptApi.get_transcript("3inFWGBsrKc&t=193s", languages=['en'])
    return srt
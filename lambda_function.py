import json
from youtube_transcript_api import YouTubeTranscriptApi

def lambda_handler(event, context):
    # TODO implement
    res = YouTubeTranscriptApi.get_transcripts(['WK4SwQaPUXM'])
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(res)
    }
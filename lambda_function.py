import json
from youtube_transcript_api import YouTubeTranscriptApi

def lambda_handler(event, context):
    list = []
    youtube_id = event['queryStringParameters']['param']
    get_data = YouTubeTranscriptApi.get_transcripts([youtube_id])
    get_list = []
    for i in get_data[0][youtube_id]:
        get_list.append(i['text'])
    str_data = ' '.join(get_list)
    dict = {'text': str_data }
    list.append(dict)
    res_data = get_data[0][youtube_id]
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(list)
    }
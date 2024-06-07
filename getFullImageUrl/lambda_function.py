import json
import requests

def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")  # 输出事件以供调试

    # 检查查询字符串参数是否存在
    if 'queryStringParameters' not in event or event['queryStringParameters'] is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No query string parameters found'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

    # 获取缩略图URL参数
    try:
        thumbnail_url = event['queryStringParameters']['thumbnail_url']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'thumbnail_url query parameter is required'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

    api_url = 'https://hc2ynd7hpb.execute-api.us-east-1.amazonaws.com/dev/5225toDB'
    response = requests.get(api_url)
    data = response.json()

    full_image_url = None
    for item in data:
        if item['ThumbnailURL'] == thumbnail_url:
            full_image_url = item['ImageURL']
            break

    if full_image_url:
        return {
            'statusCode': 200,
            'body': json.dumps({'full_image_url': full_image_url}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Thumbnail URL not found'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

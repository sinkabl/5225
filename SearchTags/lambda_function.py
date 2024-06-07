import json
import requests

def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")  # 输出事件以供调试

    # 检查查询字符串参数中是否存在标签
    try:
        tag = event['queryStringParameters']['tag']
    except (KeyError, TypeError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid request, tag is required.'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

    # API URL
    api_url = 'https://hc2ynd7hpb.execute-api.us-east-1.amazonaws.com/dev/5225toDB'
    response = requests.get(api_url)
    data = response.json()

    matching_images = [item['ImageURL'] for item in data if tag in item['Tags']]

    return {
        'statusCode': 200,
        'body': json.dumps({'matching_images': matching_images}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    }

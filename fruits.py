def handle(event, context):
    if event.method == 'GET':
        return {
            "statusCode": 200,
            "body": "GET request"
        }
    else:
        return {
            "statusCode": 405,
            "body": "Method not allowed"
        }

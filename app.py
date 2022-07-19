import json


def check(event, context):
    body = {
        "message": "Successfully executed function!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body['message'])}
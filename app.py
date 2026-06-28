def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"content-type": "text/html"},
        "body": "<h1>astrolift faas #987 live OK</h1>",
    }

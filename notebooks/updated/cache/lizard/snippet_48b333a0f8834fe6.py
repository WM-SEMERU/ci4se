def json_http_resp(handler):

    @wraps(handler)
    def wrapper(event, context):
        response = handler(event, context)
        try:
            body = json.dumps(response)
        except Exception as exception:
            return {'statusCode': 500, 'body': str(exception)}
        return {'statusCode': 200, 'body': body}
    return wrapper
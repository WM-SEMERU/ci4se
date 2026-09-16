def json_wrap(function, *args, **kwargs):
    try:
        response = json.loads(function(*args, **kwargs).content)
        if 'data' in response:
            return response['data'] or True
        else:
            return response
    except Exception as exc:
        raise ClientException(exc)
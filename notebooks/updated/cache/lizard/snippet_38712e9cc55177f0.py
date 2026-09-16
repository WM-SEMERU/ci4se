def parse(response):
    if response.status_code == 400:
        try:
            msg = json.loads(response.content)['message']
        except (KeyError, ValueError):
            msg = ''
        raise ApiError(msg)
    return response
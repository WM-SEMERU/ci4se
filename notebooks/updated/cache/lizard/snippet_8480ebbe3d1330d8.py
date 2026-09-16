def sanitize_http_request_cookies(client, event):
    try:
        cookies = event['context']['request']['cookies']
        event['context']['request']['cookies'] = varmap(_sanitize, cookies)
    except (KeyError, TypeError):
        pass
    try:
        cookie_string = event['context']['request']['headers']['cookie']
        event['context']['request']['headers']['cookie'] = _sanitize_string(
            cookie_string, '; ', '=')
    except (KeyError, TypeError):
        pass
    return event
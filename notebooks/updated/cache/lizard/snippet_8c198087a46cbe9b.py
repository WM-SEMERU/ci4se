def make_headers(keep_alive=None, accept_encoding=None, user_agent=None,
    basic_auth=None):
    headers = {}
    if accept_encoding:
        if isinstance(accept_encoding, str):
            pass
        elif isinstance(accept_encoding, list):
            accept_encoding = ','.join(accept_encoding)
        else:
            accept_encoding = 'gzip,deflate'
        headers['accept-encoding'] = accept_encoding
    if user_agent:
        headers['user-agent'] = user_agent
    if keep_alive:
        headers['connection'] = 'keep-alive'
    if basic_auth:
        headers['authorization'] = 'Basic ' + basic_auth.encode('base64'
            ).strip()
    return headers
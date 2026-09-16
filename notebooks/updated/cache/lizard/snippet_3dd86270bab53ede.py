def xauth(base_url_template=DEFAULT_READER_URL_TEMPLATE, **xargs):
    consumer_key = xargs.get('consumer_key') or required_from_env(
        'READABILITY_CONSUMER_KEY')
    consumer_secret = xargs.get('consumer_secret') or required_from_env(
        'READABILITY_CONSUMER_SECRET')
    username = xargs.get('username') or required_from_env(
        'READABILITY_USERNAME')
    password = xargs.get('password') or required_from_env(
        'READABILITY_PASSWORD')
    client = Client(consumer_key, client_secret=consumer_secret,
        signature_type='BODY')
    url = base_url_template.format(ACCESS_TOKEN_URL)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = {'x_auth_username': username, 'x_auth_password': password,
        'x_auth_mode': 'client_auth'}
    uri, headers, body = client.sign(url, http_method='POST', body=
        urlencode(params), headers=headers)
    response = requests.post(uri, data=body)
    logger.debug('POST to %s.', uri)
    token = parse_qs(response.content)
    try:
        token = token[b'oauth_token'][0].decode(), token[b'oauth_token_secret'
            ][0].decode()
    except KeyError:
        raise ValueError('Invalid Credentials.')
    return token
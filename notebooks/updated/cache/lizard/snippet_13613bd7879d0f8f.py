def from_string(s):
    if not len(s):
        raise ValueError('Invalid parameter string.')
    params = parse_qs(u(s), keep_blank_values=False)
    if not len(params):
        raise ValueError('Invalid parameter string.')
    try:
        key = params['oauth_token'][0]
    except Exception:
        raise ValueError("'oauth_token' not found in OAuth request.")
    try:
        secret = params['oauth_token_secret'][0]
    except Exception:
        raise ValueError("'oauth_token_secret' not found in OAuth request.")
    token = Token(key, secret)
    try:
        token.callback_confirmed = params['oauth_callback_confirmed'][0]
    except KeyError:
        pass
    return token
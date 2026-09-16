def get_access_token(self, request_token, request_token_secret, method=
    'GET', decoder=parse_utf8_qsl, key_token='oauth_token',
    key_token_secret='oauth_token_secret', **kwargs):
    r = self.get_raw_access_token(request_token, request_token_secret,
        method=method, **kwargs)
    access_token, access_token_secret = process_token_request(r, decoder,
        key_token, key_token_secret)
    return access_token, access_token_secret
def request_token(self):
    client_key = request.oauth.client_key
    realm = request.oauth.realm
    callback = request.oauth.callback_uri
    request_token = generate_token(length=self.request_token_length[1])
    token_secret = generate_token(length=self.secret_length)
    self.save_request_token(client_key, request_token, callback, realm=
        realm, secret=token_secret)
    return urlencode([('oauth_token', request_token), ('oauth_token_secret',
        token_secret), ('oauth_callback_confirmed', 'true')])
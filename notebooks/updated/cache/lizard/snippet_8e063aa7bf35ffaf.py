def get_access_token(self, code):
    self.token = self.oauth.fetch_token(token_url=self.access_token_url,
        client_id=self.client_id, client_secret=self.client_secret, scope=
        self.scope, code=code)
    return self.token.get('access_token')
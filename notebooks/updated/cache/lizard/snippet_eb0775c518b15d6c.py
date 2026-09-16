def get_auth_session(self, method='POST', **kwargs):
    session = self.get_session(self.get_access_token(method, **kwargs))
    if self.access_token_response:
        session.access_token_response = self.access_token_response
    return session
def creds(self):
    session = self.client.session()
    if session is None:
        return None
    return {'basic_auth': self.client.basic_auth_str(), 'user_ctx': session
        .get('userCtx')}
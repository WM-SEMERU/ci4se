def signed_session(self, session=None):
    self.set_token()
    return super(MSIAuthentication, self).signed_session(session)
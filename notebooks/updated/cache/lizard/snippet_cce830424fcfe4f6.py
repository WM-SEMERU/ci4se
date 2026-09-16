def set_session_token(self, session_token):
    self.session_token = session_token
    self._login_time = datetime.datetime.now()
def client(self):
    if self._client is None:
        self._client = get_session(self.user_agent)
    return self._client
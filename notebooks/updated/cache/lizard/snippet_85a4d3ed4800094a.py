def set_ttl(self, ttl):
    if self._client._session_timeout != ttl:
        self._client._session_timeout = ttl
        self._client.restart()
        return True
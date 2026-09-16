def _proxy(self):
    if self._context is None:
        self._context = CredentialListContext(self._version, trunk_sid=self
            ._solution['trunk_sid'], sid=self._solution['sid'])
    return self._context
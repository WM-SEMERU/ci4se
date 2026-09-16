def _proxy(self):
    if self._context is None:
        self._context = ConferenceContext(self._version, account_sid=self.
            _solution['account_sid'], sid=self._solution['sid'])
    return self._context
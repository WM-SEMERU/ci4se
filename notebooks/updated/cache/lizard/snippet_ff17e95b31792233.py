def get(self, sid):
    return AddOnResultContext(self._version, account_sid=self._solution[
        'account_sid'], reference_sid=self._solution['reference_sid'], sid=sid)
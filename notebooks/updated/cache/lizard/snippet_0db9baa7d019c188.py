def new_signing_keys(self):
    if self._new_signing_keys is None:
        self._new_signing_keys = NewSigningKeyList(self._version,
            account_sid=self._solution['sid'])
    return self._new_signing_keys
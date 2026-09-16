def keys(self):
    if self._keys is None:
        self._keys = KeyList(self._version, fleet_sid=self._solution['sid'])
    return self._keys
def assets(self):
    if self._assets is None:
        self._assets = AssetList(self._version, service_sid=self._solution[
            'sid'])
    return self._assets
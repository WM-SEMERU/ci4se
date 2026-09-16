def get(self, key):
    return SyncMapItemContext(self._version, service_sid=self._solution[
        'service_sid'], map_sid=self._solution['map_sid'], key=key)
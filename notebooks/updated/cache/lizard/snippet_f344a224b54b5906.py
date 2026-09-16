def get(self, sid):
    return SyncStreamContext(self._version, service_sid=self._solution[
        'service_sid'], sid=sid)
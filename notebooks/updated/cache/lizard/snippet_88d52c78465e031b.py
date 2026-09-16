def get(self, sid):
    return AlphaSenderContext(self._version, service_sid=self._solution[
        'service_sid'], sid=sid)
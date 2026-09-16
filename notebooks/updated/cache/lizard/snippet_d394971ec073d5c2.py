def get(self, identity):
    return DocumentPermissionContext(self._version, service_sid=self.
        _solution['service_sid'], document_sid=self._solution[
        'document_sid'], identity=identity)
def update(self, read, write, manage):
    data = values.of({'Read': read, 'Write': write, 'Manage': manage})
    payload = self._version.update('POST', self._uri, data=data)
    return SyncMapPermissionInstance(self._version, payload, service_sid=
        self._solution['service_sid'], map_sid=self._solution['map_sid'],
        identity=self._solution['identity'])
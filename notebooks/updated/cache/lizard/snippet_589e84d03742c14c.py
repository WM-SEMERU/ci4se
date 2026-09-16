def update(self, read, write, manage):
    data = values.of({'Read': read, 'Write': write, 'Manage': manage})
    payload = self._version.update('POST', self._uri, data=data)
    return SyncListPermissionInstance(self._version, payload, service_sid=
        self._solution['service_sid'], list_sid=self._solution['list_sid'],
        identity=self._solution['identity'])
def get_instance(self, payload):
    return SyncListPermissionInstance(self._version, payload, service_sid=
        self._solution['service_sid'], list_sid=self._solution['list_sid'])
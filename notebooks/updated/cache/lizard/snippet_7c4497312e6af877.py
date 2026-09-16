def sync_map_permissions(self):
    if self._sync_map_permissions is None:
        self._sync_map_permissions = SyncMapPermissionList(self._version,
            service_sid=self._solution['service_sid'], map_sid=self.
            _solution['sid'])
    return self._sync_map_permissions
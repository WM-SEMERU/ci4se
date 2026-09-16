def sync_maps(self):
    if self._sync_maps is None:
        self._sync_maps = SyncMapList(self._version, service_sid=self.
            _solution['sid'])
    return self._sync_maps
def sync_map_items(self):
    if self._sync_map_items is None:
        self._sync_map_items = SyncMapItemList(self._version, service_sid=
            self._solution['service_sid'], map_sid=self._solution['sid'])
    return self._sync_map_items
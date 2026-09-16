def storage_groups(self):
    if not self._storage_groups:
        self._storage_groups = StorageGroupManager(self)
    return self._storage_groups
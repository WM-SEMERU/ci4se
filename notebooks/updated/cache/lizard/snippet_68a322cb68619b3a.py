def _flush_data(self):
    if self._data and self._data.modified:
        hookenv.relation_set(self.relation_id, dict(self.to_publish.data))
def _save(self):
    yield self.validate()
    db = self.db_client()
    saved = yield db.save_doc(self._resource)
    if '_id' not in self._resource:
        self._resource['_id'] = saved['id']
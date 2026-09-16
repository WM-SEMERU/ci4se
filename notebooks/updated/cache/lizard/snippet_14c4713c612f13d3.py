def _find_batch_containing_event(self, uuid):
    if self.estore.key_exists(uuid):
        return self.batchno
    else:
        for batchno in range(self.batchno - 1, -1, -1):
            db = self._open_event_store(batchno)
            with contextlib.closing(db):
                if db.key_exists(uuid):
                    return batchno
    return None
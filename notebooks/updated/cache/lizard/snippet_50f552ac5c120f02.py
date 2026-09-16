def watch(self, key, pipeline=False):
    if pipeline:
        self._pipeline.watch(key)
    else:
        self._db.watch(key)
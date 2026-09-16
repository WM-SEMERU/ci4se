def verify(self):
    if self._lock != 0:
        return
    id_new = self._id_function()
    if id_new != self.id_current:
        if len(self.cache) > 0:
            log.debug('%d items cleared from cache: %s', len(self.cache),
                str(list(self.cache.keys())))
        self.cache = {}
        self.id_current = id_new
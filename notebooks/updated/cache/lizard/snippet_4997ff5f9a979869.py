def put(self, key, data):
    try:
        return self._dstore.put(key, data)
    finally:
        self.cache.delete(key)
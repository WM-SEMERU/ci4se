def put(self, key, value):
    self.cache_datastore.put(key, value)
    self.child_datastore.put(key, value)
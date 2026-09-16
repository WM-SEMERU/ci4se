def set(self, key, value, timeout=None):
    key = self.make_key(key)
    if timeout is None:
        timeout = self.default_timeout
    if self.debug:
        return True
    pickled_value = pickle.dumps(value)
    self.metrics['writes'] += 1
    if timeout:
        return self.database.setex(key, int(timeout), pickled_value)
    else:
        return self.database.set(key, pickled_value)
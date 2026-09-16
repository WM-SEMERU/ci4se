def locked_get_or_set(self, key, value_creator, version=None, expire=None,
    id=None, lock_key=None, timeout=DEFAULT_TIMEOUT):
    if lock_key is None:
        lock_key = 'get_or_set:' + key
    val = self.get(key, version=version)
    if val is not None:
        return val
    with self.lock(lock_key, expire=expire, id=id):
        val = self.get(key, version=version)
        if val is not None:
            return val
        val = value_creator()
        if val is None:
            raise ValueError('`value_creator` must return a value')
        self.set(key, val, timeout=timeout, version=version)
        return val
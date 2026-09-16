def add(self, key, val, minutes):
    if hasattr(self._store, 'add'):
        return self._store.add(key, val, self._get_minutes(minutes))
    if not self.has(key):
        self.put(key, val, minutes)
        return True
    return False
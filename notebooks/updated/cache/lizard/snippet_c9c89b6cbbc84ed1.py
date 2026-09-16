def get(self, key, bucket):
    try:
        return self._cache[bucket][key]
    except (KeyError, TypeError):
        return None
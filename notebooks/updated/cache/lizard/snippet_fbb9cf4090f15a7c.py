def expire(self, key, delta):
    delta = delta if isinstance(delta, timedelta) else timedelta(seconds=delta)
    return self._expire(self._encode(key), delta)
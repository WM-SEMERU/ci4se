def getKeyConfig(self, keyID=None):
    k = keyID if keyID is not None else self._keyID
    if not k or k not in self._data['keys']:
        raise ConfigException('request key does not exist: %s' % k)
    return self._data['keys'][k]
def load(self, id):
    l.debug('LOAD: %s', id)
    try:
        l.debug('... trying cached')
        return self._object_cache[id]
    except KeyError:
        l.debug('... cached failed')
        with self._read_context(id) as u:
            return VaultUnpickler(self, u).load()
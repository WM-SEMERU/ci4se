def update_metadata(self, key, value):
    old_value = self.contents['metadata'].get(key)
    self.contents['metadata'][key] = value
    self._log('Updated metadata: %s=%s' % (key, value))
    return old_value
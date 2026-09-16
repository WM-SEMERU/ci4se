def __prefix_key(self, key):
    if self.prefix is None:
        return key
    if key.startswith(self.prefix + '-'):
        return key
    return '{0}-{1}'.format(self.prefix, key)
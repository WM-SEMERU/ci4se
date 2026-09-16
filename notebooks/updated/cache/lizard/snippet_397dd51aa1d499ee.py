def _items(self, type_filter=None, name=None):
    if name:
        if type_filter and self._key_attr == 'type':
            if name in type_filter and name in self:
                yield name, self[name]
        elif name in self:
            yield name, self[name]
    elif type_filter and self._key_attr == 'type':
        for key, val in self.items():
            if key in type_filter:
                yield key, val
    else:
        for key, val in self.items():
            yield key, val
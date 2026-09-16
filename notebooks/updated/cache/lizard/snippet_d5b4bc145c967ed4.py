def with_name(self, name):
    if not self.name:
        raise ValueError('%r has an empty name' % (self,))
    return self._from_parsed_parts(self._drv, self._root, self._parts[:-1] +
        [name])
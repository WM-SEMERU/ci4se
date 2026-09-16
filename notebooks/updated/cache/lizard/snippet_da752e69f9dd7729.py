def structure_repr(self):
    ret = '{%s}' % ', '.join([str(x) for x in self.elements])
    return self._wrap_packed(ret)
def envCheckFilter(self, name, attr):
    flt = self._filters.get(name)
    if flt:
        return flt.check(attr)
    else:
        raise AttributeError('Undefined filter: %s' % name)
def save(self, clean=True):
    ret = {}
    if clean:
        self._dirty = False
    else:
        ret['_dirty'] = self._dirty
    return ret
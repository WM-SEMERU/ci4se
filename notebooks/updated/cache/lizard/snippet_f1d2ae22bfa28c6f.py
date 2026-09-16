def matches(self, event):
    ret = []
    self._matches(event, set(), ret)
    return tuple(r[0] for r in ret)
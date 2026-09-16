def waiters(self, path=None):
    context = self._waiters
    if path is None:
        path = []
    for key in path:
        context = context[key]
    if self._LEAF in context:
        for future in context[self._LEAF]:
            yield path, future
    for key in context:
        if key is self._LEAF:
            continue
        yield from self.waiters(path=path + [key])
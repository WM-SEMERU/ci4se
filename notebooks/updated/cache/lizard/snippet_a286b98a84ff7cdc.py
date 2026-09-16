def get_provides(self, ignored=tuple()):
    if self._provides is None:
        self._collect_requires_provides()
    d = self._provides
    if ignored:
        d = dict((k, v) for k, v in d.items() if not fnmatches(k, *ignored))
    return d
def to_dict(self, **kwargs):
    d = {}
    if self.query:
        d['query'] = self.query.to_dict()
    if self._script:
        d['script'] = self._script
    d.update(self._extra)
    d.update(kwargs)
    return d
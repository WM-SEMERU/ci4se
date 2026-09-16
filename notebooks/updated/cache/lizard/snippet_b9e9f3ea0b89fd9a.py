def add_tags(self, tags, **kwargs):
    self._add_tags(self._dxid, {'project': self._proj, 'tags': tags}, **kwargs)
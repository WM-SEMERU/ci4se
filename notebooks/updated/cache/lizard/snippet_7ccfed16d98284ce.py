def _unset(self, pos):
    assert 0 <= pos < self.len
    self._datastore.unsetbit(pos)
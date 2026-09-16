def remove(self, safe=None):
    self._session.remove(self, safe=None)
    self._session.flush()
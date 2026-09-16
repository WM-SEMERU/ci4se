def _store(self, con):
    self._con = con
    self._transaction = False
    self._closed = False
    self._usage = 0
def clear(self):
    if len(self.list):
        self._LOG.debug('List cleared.')
    self.list.clear()
def _processor(self):
    self.store.cleanup(self._config.timeout)
    self._load()
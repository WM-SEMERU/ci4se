def adapters(self):
    if not self._adapters:
        self._adapters = AdapterManager(self)
    return self._adapters
def reload(self):
    for loader in self._loaders:
        loader.reload()
    self.varz = {}
    self._load()
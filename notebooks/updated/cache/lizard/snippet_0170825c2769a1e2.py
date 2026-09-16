def load(self, modelfile, layer=None):
    self.param_file = modelfile
    self._load(layer)
    self._update(layer)
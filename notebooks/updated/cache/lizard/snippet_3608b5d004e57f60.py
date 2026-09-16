def setValidated(self, state):
    self._validated = state
    palette = self.palette()
    self._filepathEdit.setPalette(palette)
    self.validate()
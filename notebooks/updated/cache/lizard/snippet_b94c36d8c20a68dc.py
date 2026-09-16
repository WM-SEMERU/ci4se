def model(self):
    if self._model is None and self.parentItem is not None:
        self._model = self.parentItem.model
    return self._model
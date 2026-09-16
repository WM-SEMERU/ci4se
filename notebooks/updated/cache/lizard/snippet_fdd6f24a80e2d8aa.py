def build(self):
    if self.is_built():
        return
    with _wait_signal(self.loadFinished, 20):
        self.rebuild()
    self._built = True
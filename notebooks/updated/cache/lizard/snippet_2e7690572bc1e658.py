def setAnimated(self, state):
    self._animated = state
    self.setAttribute(Qt.WA_TranslucentBackground, state)
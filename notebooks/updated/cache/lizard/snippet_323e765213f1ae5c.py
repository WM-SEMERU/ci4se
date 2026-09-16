def setAutoDefault(self, state):
    self._autoDefault = state
    for button in self.buttonBox().buttons():
        button.setAutoDefault(state)
        button.setDefault(state)
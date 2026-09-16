def setEditable(self, state):
    self._editable = state
    if state:
        self.setEditTriggers(self.AllEditTriggers)
    else:
        self.setEditTriggers(self.NoEditTriggers)
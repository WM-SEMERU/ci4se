def setShowHours(self, state=True):
    self._showHours = state
    if state:
        self._hourSeparator.show()
        self._hourCombo.show()
    else:
        self._hourSeparator.hide()
        self._hourCombo.hide()
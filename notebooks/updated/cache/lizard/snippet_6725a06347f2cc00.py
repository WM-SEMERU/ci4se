def blockSignals(self, state):
    super(XUrlWidget, self).blockSignals(state)
    self._urlEdit.blockSignals(state)
    self._urlButton.blockSignals(state)
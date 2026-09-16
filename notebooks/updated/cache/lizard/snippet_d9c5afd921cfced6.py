def focusInEvent(self, event):
    self._changedRecord = -1
    super(XOrbRecordBox, self).focusInEvent(event)
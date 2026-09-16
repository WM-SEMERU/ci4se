def saveSilent(self):
    self.blockSignals(True)
    success = self.save()
    self.blockSignals(False)
    return success
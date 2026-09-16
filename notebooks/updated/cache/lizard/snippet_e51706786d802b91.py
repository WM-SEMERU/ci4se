def setAlignment(self, align):
    self.blockSignals(True)
    self.editor().setAlignment(align)
    self.blockSignals(False)
    self.refreshAlignmentUi()
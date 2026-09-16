def on_leTitle_textChanged(self):
    self.parent.pbnNext.setEnabled(bool(self.leTitle.text()))
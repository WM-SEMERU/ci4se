def focusOutEvent(self, event):
    self.focus_changed.emit()
    QPlainTextEdit.focusOutEvent(self, event)
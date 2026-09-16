def focusInEvent(self, event):
    self.focus_changed.emit()
    return super(PageControlWidget, self).focusInEvent(event)
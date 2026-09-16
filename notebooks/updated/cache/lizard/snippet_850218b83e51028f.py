def focusInEvent(self, event):
    widget = self.widget
    type(widget).focusInEvent(widget, event)
    self.declaration.focus_gained()
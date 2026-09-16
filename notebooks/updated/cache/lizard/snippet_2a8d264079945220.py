def mouseMoveEvent(self, event):
    self.line_number_hint = self.editor.get_linenumber_from_mouse_event(event)
    self.update()
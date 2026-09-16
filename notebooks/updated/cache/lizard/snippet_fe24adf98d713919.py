def mousePressEvent(self, event):
    line_number = self.editor.get_linenumber_from_mouse_event(event)
    self._pressed = line_number
    self._released = line_number
    self.editor.select_lines(self._pressed, self._released)
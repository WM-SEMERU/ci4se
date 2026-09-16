def clear(self):
    self.erase()
    output = self.output
    output.erase_screen()
    output.cursor_goto(0, 0)
    output.flush()
    self.request_absolute_cursor_position()
def text_input(self, window, allow_resize=False):
    window.clear()
    self.curs_set(1)
    textbox = textpad.Textbox(window)
    textbox.stripspaces = 0

    def validate(ch):
        """Filters characters for special key sequences"""
        if ch == self.ESCAPE:
            raise exceptions.EscapeInterrupt()
        if not allow_resize and ch == curses.KEY_RESIZE:
            raise exceptions.EscapeInterrupt()
        if ch == curses.ascii.DEL:
            ch = curses.KEY_BACKSPACE
        return ch
    try:
        out = textbox.edit(validate=validate)
        if isinstance(out, six.binary_type):
            out = out.decode('utf-8')
    except exceptions.EscapeInterrupt:
        out = None
    self.curs_set(0)
    return self.strip_textpad(out)
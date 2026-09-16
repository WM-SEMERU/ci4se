def get_cursor_vertical_diff(self):
    if self.in_get_cursor_diff:
        self.another_sigwinch = True
        return 0
    cursor_dy = 0
    while True:
        self.in_get_cursor_diff = True
        self.another_sigwinch = False
        cursor_dy += self._get_cursor_vertical_diff_once()
        self.in_get_cursor_diff = False
        if not self.another_sigwinch:
            return cursor_dy
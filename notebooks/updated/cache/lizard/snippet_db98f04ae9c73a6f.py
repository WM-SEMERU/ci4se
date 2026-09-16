def set_cursor_x(self, x):
    if x >= 0 and x <= self.server.server_info.get('screen_width'):
        self.cursor_x = x
        self.server.request('screen_set %s cursor_x %i' % (self.ref, self.
            cursor_x))
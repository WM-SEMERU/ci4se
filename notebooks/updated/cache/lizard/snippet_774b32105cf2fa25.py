def cursor_pagedown(self, stats):
    if self._current_page + 1 < self._page_max:
        self._current_page += 1
    else:
        self._current_page = 0
    self.cursor_position = 0
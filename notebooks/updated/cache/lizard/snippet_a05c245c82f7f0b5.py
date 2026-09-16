def update_cursor(self, dc, grid, row, col):
    old_row, old_col = self.old_cursor_row_col
    bgcolor = get_color(config['background_color'])
    self._draw_cursor(dc, grid, old_row, old_col, pen=wx.Pen(bgcolor),
        brush=wx.Brush(bgcolor))
    self._draw_cursor(dc, grid, row, col)
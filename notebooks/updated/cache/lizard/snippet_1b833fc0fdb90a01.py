def rectangle(self, x, y, width, height):
    cairo.cairo_rectangle(self._pointer, x, y, width, height)
    self._check_status()
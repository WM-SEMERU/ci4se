def add_color_stop_rgba(self, offset, red, green, blue, alpha=1):
    cairo.cairo_pattern_add_color_stop_rgba(self._pointer, offset, red,
        green, blue, alpha)
    self._check_status()
def set_antialias(self, antialias):
    cairo.cairo_font_options_set_antialias(self._pointer, antialias)
    self._check_status()
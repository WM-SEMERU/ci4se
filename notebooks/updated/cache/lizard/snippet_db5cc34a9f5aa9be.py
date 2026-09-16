def set_fill_rule(self, fill_rule):
    cairo.cairo_set_fill_rule(self._pointer, fill_rule)
    self._check_status()
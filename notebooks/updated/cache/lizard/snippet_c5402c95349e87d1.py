def set_hint_metrics(self, hint_metrics):
    cairo.cairo_font_options_set_hint_metrics(self._pointer, hint_metrics)
    self._check_status()
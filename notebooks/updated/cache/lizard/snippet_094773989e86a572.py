def get_font_matrix(self):
    matrix = Matrix()
    cairo.cairo_scaled_font_get_font_matrix(self._pointer, matrix._pointer)
    self._check_status()
    return matrix
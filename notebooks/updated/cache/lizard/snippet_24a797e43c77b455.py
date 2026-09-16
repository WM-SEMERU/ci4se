def font_extents(self):
    extents = ffi.new('cairo_font_extents_t *')
    cairo.cairo_font_extents(self._pointer, extents)
    self._check_status()
    return (extents.ascent, extents.descent, extents.height, extents.
        max_x_advance, extents.max_y_advance)
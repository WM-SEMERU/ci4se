def text_extents(self, text):
    extents = ffi.new('cairo_text_extents_t *')
    cairo.cairo_text_extents(self._pointer, _encode_string(text), extents)
    self._check_status()
    return (extents.x_bearing, extents.y_bearing, extents.width, extents.
        height, extents.x_advance, extents.y_advance)
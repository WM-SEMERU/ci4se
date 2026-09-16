def copy(self):
    cls = type(self)
    other = object.__new__(cls)
    cls._init_pointer(other, cairo.cairo_font_options_copy(self._pointer))
    return other
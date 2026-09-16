def create_from_png(cls, source):
    if hasattr(source, 'read'):
        read_func = _make_read_func(source)
        pointer = cairo.cairo_image_surface_create_from_png_stream(read_func,
            ffi.NULL)
    else:
        pointer = cairo.cairo_image_surface_create_from_png(_encode_filename
            (source))
    self = object.__new__(cls)
    Surface.__init__(self, pointer)
    return self
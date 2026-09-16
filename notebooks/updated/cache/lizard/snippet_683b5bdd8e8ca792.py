def get_mime_data(self, mime_type):
    buffer_address = ffi.new('unsigned char **')
    buffer_length = ffi.new('unsigned long *')
    mime_type = ffi.new('char[]', mime_type.encode('utf8'))
    cairo.cairo_surface_get_mime_data(self._pointer, mime_type,
        buffer_address, buffer_length)
    return ffi.buffer(buffer_address[0], buffer_length[0]) if buffer_address[0
        ] != ffi.NULL else None
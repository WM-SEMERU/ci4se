def supports_mime_type(self, mime_type):
    mime_type = ffi.new('char[]', mime_type.encode('utf8'))
    return bool(cairo.cairo_surface_supports_mime_type(self._pointer,
        mime_type))
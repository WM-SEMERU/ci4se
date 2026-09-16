def pixbuf_to_cairo_png(pixbuf):
    buffer_pointer = ffi.new('gchar **')
    buffer_size = ffi.new('gsize *')
    error = ffi.new('GError **')
    handle_g_error(error, pixbuf.save_to_buffer(buffer_pointer, buffer_size,
        ffi.new('char[]', b'png'), error, ffi.new('char[]', b'compression'),
        ffi.new('char[]', b'0'), ffi.NULL))
    png_bytes = ffi.buffer(buffer_pointer[0], buffer_size[0])
    return ImageSurface.create_from_png(BytesIO(png_bytes))
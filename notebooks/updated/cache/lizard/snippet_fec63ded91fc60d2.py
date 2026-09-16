def copy(self, texture, source_rect=None, dest_rect=None, rotation=0,
    center=None, flip=lib.SDL_FLIP_NONE):
    if source_rect == None:
        source_rect_ptr = ffi.NULL
    else:
        source_rect_ptr = source_rect._ptr
    if dest_rect == None:
        dest_rect_ptr = ffi.NULL
    else:
        dest_rect_ptr = dest_rect._ptr
    if center == None:
        center_ptr = ffi.NULL
    else:
        center_ptr = center._ptr
    check_int_err(lib.SDL_RenderCopyEx(self._ptr, texture._ptr,
        source_rect_ptr, dest_rect_ptr, rotation, center_ptr, flip))
def w(self):
    w = ffi.new('int *')
    check_int_err(lib.SDL_QueryTexture(self._ptr, ffi.NULL, ffi.NULL, w,
        ffi.NULL))
    return w[0]
def get_window_name(self, win_id):
    window = window_t(win_id)
    name_ptr = ctypes.c_char_p()
    name_len = ctypes.c_int(0)
    name_type = ctypes.c_int(0)
    _libxdo.xdo_get_window_name(self._xdo, window, ctypes.byref(name_ptr),
        ctypes.byref(name_len), ctypes.byref(name_type))
    name = name_ptr.value
    _libX11.XFree(name_ptr)
    return name
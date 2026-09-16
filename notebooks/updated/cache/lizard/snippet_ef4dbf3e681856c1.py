def get_mouse_location(self):
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)
    screen_num = ctypes.c_int(0)
    _libxdo.xdo_get_mouse_location(self._xdo, ctypes.byref(x), ctypes.byref
        (y), ctypes.byref(screen_num))
    return mouse_location(x.value, y.value, screen_num.value)
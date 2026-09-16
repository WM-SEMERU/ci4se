def get_active_window(self):
    window_ret = window_t(0)
    _libxdo.xdo_get_active_window(self._xdo, ctypes.byref(window_ret))
    return window_ret.value
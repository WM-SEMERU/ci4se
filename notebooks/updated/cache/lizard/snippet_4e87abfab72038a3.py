def get_focused_window_sane(self):
    window_ret = window_t(0)
    _libxdo.xdo_get_focused_window_sane(self._xdo, ctypes.byref(window_ret))
    return window_ret.value
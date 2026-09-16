def set_window_property(self, window, name, value):
    _libxdo.xdo_set_window_property(self._xdo, window, name, value)
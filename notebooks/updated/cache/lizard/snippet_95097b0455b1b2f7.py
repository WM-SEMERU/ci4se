def enter_text_window(self, window, string, delay=12000):
    return _libxdo.xdo_enter_text_window(self._xdo, window, string, delay)
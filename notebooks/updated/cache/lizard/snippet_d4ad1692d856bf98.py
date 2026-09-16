def show(self, block_command_line=False, block_timing=0.05):
    self._is_open = True
    self._window.show()
    self._window.raise_()
    if block_command_line:
        while self._is_open:
            _a.processEvents()
            _t.sleep(block_timing)
        _t.sleep(0.5)
    return self
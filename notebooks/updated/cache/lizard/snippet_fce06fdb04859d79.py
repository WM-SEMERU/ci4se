def _mouseDown(x, y, button):
    if button == 'left':
        try:
            _sendMouseEvent(MOUSEEVENTF_LEFTDOWN, x, y)
        except (PermissionError, OSError):
            pass
    elif button == 'middle':
        try:
            _sendMouseEvent(MOUSEEVENTF_MIDDLEDOWN, x, y)
        except (PermissionError, OSError):
            pass
    elif button == 'right':
        try:
            _sendMouseEvent(MOUSEEVENTF_RIGHTDOWN, x, y)
        except (PermissionError, OSError):
            pass
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"
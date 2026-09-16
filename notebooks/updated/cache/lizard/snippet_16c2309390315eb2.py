def focusWindow(self, hwnd):
    Debug.log(3, 'Focusing window: ' + str(hwnd))
    SW_RESTORE = 9
    if ctypes.windll.user32.IsIconic(hwnd):
        ctypes.windll.user32.ShowWindow(hwnd, SW_RESTORE)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
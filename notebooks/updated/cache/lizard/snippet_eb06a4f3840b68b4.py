def getWindows():
    titles = {}

    def foreach_window(hwnd, lparam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles[buff.value] = hwnd
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return titles
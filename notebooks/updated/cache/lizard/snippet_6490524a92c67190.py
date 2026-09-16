def get_info(handle):
    csbi = _WindowsCSBI.CSBI()
    try:
        if not _WindowsCSBI.WINDLL.kernel32.GetConsoleScreenBufferInfo(handle,
            ctypes.byref(csbi)):
            raise IOError(
                'Unable to get console screen buffer info from win32 API.')
    except ctypes.ArgumentError:
        raise IOError(
            'Unable to get console screen buffer info from win32 API.')
    result = dict(buffer_width=int(csbi.dwSize.X - 1), buffer_height=int(
        csbi.dwSize.Y), terminal_width=int(csbi.srWindow.Right - csbi.
        srWindow.Left), terminal_height=int(csbi.srWindow.Bottom - csbi.
        srWindow.Top), bg_color=int(csbi.wAttributes & 240), fg_color=int(
        csbi.wAttributes % 16))
    return result
def OpenDevice(path, enum=False):
    desired_access = GENERIC_WRITE | GENERIC_READ
    share_mode = FILE_SHARE_READ | FILE_SHARE_WRITE
    if enum:
        desired_access = 0
    h = kernel32.CreateFileA(path, desired_access, share_mode, None,
        OPEN_EXISTING, 0, None)
    if h == INVALID_HANDLE_VALUE:
        raise ctypes.WinError()
    return h
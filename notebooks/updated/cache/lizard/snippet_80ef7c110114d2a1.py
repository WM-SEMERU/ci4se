def set_windows_env_var(key, value):
    if not isinstance(key, text_type):
        raise TypeError('%r not of type %r' % (key, text_type))
    if not isinstance(value, text_type):
        raise TypeError('%r not of type %r' % (value, text_type))
    status = winapi.SetEnvironmentVariableW(key, value)
    if status == 0:
        raise ctypes.WinError()
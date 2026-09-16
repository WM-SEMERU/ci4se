def set_windows_dll_path():
    lib_path = os.path.dirname(os.path.abspath(_pylambda_worker.__file__))
    lib_path = os.path.abspath(os.path.join(lib_path, os.pardir))

    def errcheck_bool(result, func, args):
        if not result:
            last_error = ctypes.get_last_error()
            if last_error != 0:
                raise ctypes.WinError(last_error)
            else:
                raise OSError
        return args
    import ctypes.wintypes as wintypes
    try:
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel32.SetDllDirectoryW.errcheck = errcheck_bool
        kernel32.SetDllDirectoryW.argtypes = wintypes.LPCWSTR,
        kernel32.SetDllDirectoryW(lib_path)
    except Exception as e:
        logging.getLogger(__name__).warning(
            'Error setting DLL load orders: %s (things should still work).' %
            str(e))
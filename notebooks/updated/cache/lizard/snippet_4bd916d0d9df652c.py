def get_nt_7z_dir():
    try:
        import _winreg as winreg
    except ImportError:
        import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\7-Zip')
        try:
            return winreg.QueryValueEx(key, 'Path')[0]
        finally:
            winreg.CloseKey(key)
    except WindowsError:
        return ''
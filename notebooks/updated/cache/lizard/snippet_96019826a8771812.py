def parse_bdist_wininst(name):
    lower = name.lower()
    base, py_ver, plat = None, None, None
    if lower.endswith('.exe'):
        if lower.endswith('.win32.exe'):
            base = name[:-10]
            plat = 'win32'
        elif lower.startswith('.win32-py', -16):
            py_ver = name[-7:-4]
            base = name[:-16]
            plat = 'win32'
        elif lower.endswith('.win-amd64.exe'):
            base = name[:-14]
            plat = 'win-amd64'
        elif lower.startswith('.win-amd64-py', -20):
            py_ver = name[-7:-4]
            base = name[:-20]
            plat = 'win-amd64'
    return base, py_ver, plat
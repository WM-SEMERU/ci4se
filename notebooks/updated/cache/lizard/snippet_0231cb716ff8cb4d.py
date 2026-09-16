def is_modern_windows_install(version):
    version = LooseVersion(str(version))
    if is_win() and version >= LooseVersion('2.1'):
        return True
    else:
        return False
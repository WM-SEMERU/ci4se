def _getRegisteredExecutable(exeName):
    registered = None
    if sys.platform.startswith('win'):
        if os.path.splitext(exeName)[1].lower() != '.exe':
            exeName += '.exe'
        import _winreg
        try:
            key = (
                'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\' +
                exeName)
            value = _winreg.QueryValue(_winreg.HKEY_LOCAL_MACHINE, key)
            registered = value, 'from HKLM\\' + key
        except _winreg.error:
            pass
        if registered and not os.path.exists(registered[0]):
            registered = None
    return registered
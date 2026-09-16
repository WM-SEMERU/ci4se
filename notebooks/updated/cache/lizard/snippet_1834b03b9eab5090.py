def arduino_default_path():
    if sys.platform == 'darwin':
        s = path('/Applications/Arduino.app/Contents/Resources/Java')
    elif sys.platform == 'win32':
        s = None
    else:
        s = path('/usr/share/arduino/')
    return s
def id(self):
    try:
        return os.environ['BLINKA_FORCECHIP']
    except KeyError:
        pass
    try:
        if os.environ['BLINKA_FT232H']:
            import ftdi1 as ftdi
            try:
                ctx = None
                ctx = ftdi.new()
                count, _ = ftdi.usb_find_all(ctx, 0, 0)
                if count < 0:
                    raise RuntimeError(
                        'ftdi_usb_find_all returned error %d : %s' % count,
                        ftdi.get_error_string(self._ctx))
                if count == 0:
                    raise RuntimeError('BLINKA_FT232H environment variable' +
                        'set, but no FT232H device found')
            finally:
                if ctx is not None:
                    ftdi.free(ctx)
        return FT232H
    except KeyError:
        pass
    platform = sys.platform
    if platform == 'linux' or platform == 'linux2':
        return self._linux_id()
    if platform == 'esp8266':
        return ESP8266
    if platform == 'samd21':
        return SAMD21
    if platform == 'pyboard':
        return STM32
    return None
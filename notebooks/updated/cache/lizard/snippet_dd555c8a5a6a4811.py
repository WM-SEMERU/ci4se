def read(self):
    try:
        buf = os.read(self._fd, 8)
    except OSError as e:
        raise LEDError(e.errno, 'Reading LED brightness: ' + e.strerror)
    try:
        os.lseek(self._fd, 0, os.SEEK_SET)
    except OSError as e:
        raise LEDError(e.errno, 'Rewinding LED brightness: ' + e.strerror)
    return int(buf)
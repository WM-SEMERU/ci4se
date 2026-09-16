def _GetCh(self):
    fd = self._tty.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = self._tty.read(1)
        if ord(ch) == 27:
            ch += self._tty.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch
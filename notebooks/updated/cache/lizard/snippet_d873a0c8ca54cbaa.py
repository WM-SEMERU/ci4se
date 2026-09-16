def getch(self):
    return NotImplemented
    fno = stdout.fileno()
    mode = self.termios.tcgetattr(fno)
    try:
        self.tty.setraw(fno, self.termios.TCSANOW)
        ch = self.read(1)
    finally:
        self.termios.tcsetattr(fno, self.termios.TCSANOW, mode)
    return ch
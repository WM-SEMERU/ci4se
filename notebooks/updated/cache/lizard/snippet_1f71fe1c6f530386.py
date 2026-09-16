def raw_mode():
    if WIN:
        yield
    else:
        import tty
        import termios
        if not isatty(sys.stdin):
            f = open('/dev/tty')
            fd = f.fileno()
        else:
            fd = sys.stdin.fileno()
            f = None
        try:
            old_settings = termios.tcgetattr(fd)
            tty.setraw(fd)
        except termios.error:
            pass
        try:
            yield
        finally:
            try:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                if f is not None:
                    f.close()
            except termios.error:
                pass
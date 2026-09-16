def _getch():
    import tty
    with TermStack() as fd:
        tty.setraw(fd)
        return sys.stdin.read(1)
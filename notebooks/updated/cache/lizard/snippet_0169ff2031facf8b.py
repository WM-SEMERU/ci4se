def console_size(fd=1):
    try:
        import fcntl
        import termios
        import struct
    except ImportError:
        size = os.getenv('LINES', 25), os.getenv('COLUMNS', 80)
    else:
        size = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, b'1234')
            )
    return size
def frames_iter(socket, tty):
    if tty:
        return ((STDOUT, frame) for frame in frames_iter_tty(socket))
    else:
        return frames_iter_no_tty(socket)
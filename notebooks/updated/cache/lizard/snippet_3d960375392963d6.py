def communicate(sock, command, settings=[]):
    try:
        COMMUNICATE_LOCK.acquire()
        write_packet(sock, command)
        for option in settings:
            write_packet(sock, option)
        return read_packet(sock)
    finally:
        COMMUNICATE_LOCK.release()
def nl_socket_set_buffer_size(sk, rxbuf, txbuf):
    rxbuf = 32768 if rxbuf <= 0 else rxbuf
    txbuf = 32768 if txbuf <= 0 else txbuf
    if sk.s_fd == -1:
        return -NLE_BAD_SOCK
    try:
        sk.socket_instance.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,
            txbuf)
    except OSError as exc:
        return -nl_syserr2nlerr(exc.errno)
    try:
        sk.socket_instance.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF,
            rxbuf)
    except OSError as exc:
        return -nl_syserr2nlerr(exc.errno)
    sk.s_flags |= NL_SOCK_BUFSIZE_SET
    return 0
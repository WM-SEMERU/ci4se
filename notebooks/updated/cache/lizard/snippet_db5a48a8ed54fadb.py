def socket_set_hwm(socket, hwm=-1):
    try:
        socket.sndhwm = socket.rcvhwm = hwm
    except AttributeError:
        socket.hwm = hwm
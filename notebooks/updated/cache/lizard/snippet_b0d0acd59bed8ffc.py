def create_socket():
    sock = socket.socket(PF_CAN, socket.SOCK_RAW, CAN_RAW)
    log.info('Created a socket')
    return sock
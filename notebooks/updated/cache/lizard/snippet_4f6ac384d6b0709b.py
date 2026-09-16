def socket_send(sock, msg, debug=False):
    if IS_PY2:
        sock.send(msg)
    else:
        sock.send(msg.encode())
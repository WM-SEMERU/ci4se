def connect():
    global adb_socket
    if adb_socket is not None:
        raise RuntimeError('connection already existed')
    host, port = config.HOST, config.PORT
    connection = socket.socket()
    try:
        connection.connect((host, port))
    except ConnectionError as _:
        warn_msg = ('failed when connecting to adb server: {}:{}, retrying ...'
            .format(host, port))
        warnings.warn(warn_msg)
        reboot_adb_server()
        connect()
        return
    adb_socket = connection
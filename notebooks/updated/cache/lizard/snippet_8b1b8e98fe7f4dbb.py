def await_connection(host, port):
    for i in range(CONNECT_ATTEMPTS):
        try:
            conn = socket.create_connection((host, port), CONNECT_TIMEOUT)
            conn.close()
            return True
        except (IOError, socket.error):
            time.sleep(1)
    return False
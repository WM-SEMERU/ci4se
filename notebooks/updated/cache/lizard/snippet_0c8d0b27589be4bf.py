def __check_port(self, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((_host(), port))
        return True
    except socket.error:
        return False
    finally:
        s.close()
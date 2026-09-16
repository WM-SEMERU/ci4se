def close_socket(self):
    try:
        self.docker_py_sock._sock.close()
    except AttributeError:
        pass
    self.docker_py_sock.close()
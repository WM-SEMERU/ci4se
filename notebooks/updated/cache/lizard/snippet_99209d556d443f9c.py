def _init_listen_socket(self):
    self.debug('()')
    self._listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self._listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self._listen_socket.bind((self._listen_ip, self._listen_port))
    self._listening.append(self._listen_socket)
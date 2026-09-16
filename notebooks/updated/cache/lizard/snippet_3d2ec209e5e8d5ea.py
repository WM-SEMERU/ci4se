def _close_kernel_socket(self):
    if six.PY2 and hasattr(self.socket, '_sock'):
        self.socket._sock.close()
def get_file_descriptor(self):
    return (self._subscription.connection and self._subscription.connection
        ._sock.fileno())
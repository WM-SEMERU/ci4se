def close(self):
    if self._connection:
        self._connection_file.close()
        self._connection_file = None
        self._connection.close()
        self._connection = None
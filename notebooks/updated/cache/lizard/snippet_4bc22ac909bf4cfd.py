def _write_bytes(self, data):
    with self.__lock:
        self.output.write(to_bytes(data, self.encoding))
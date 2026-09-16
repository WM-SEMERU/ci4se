def get(self):
    data = b''
    with self.lock:
        data, self.buf = self.buf, b''
    return data
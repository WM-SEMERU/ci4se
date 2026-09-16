def read(self):
    with closing(self.open()) as f:
        data = f.read()
    return data.decode('utf-8') or None
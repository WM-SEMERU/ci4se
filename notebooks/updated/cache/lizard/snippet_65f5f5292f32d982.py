def write(self, data):
    if not data:
        return None
    self.buffer += data
    self.do_write()
    return len(data)
def flush_records(self):
    s = b''.join(p.raw_stateful() for p in self.buffer_out)
    self.socket.send(s)
    self.buffer_out = []
def read(self):
    self.repr_.setvalue(ord(self.open_stream_in.read(1)))
    return self.value.getvalue()
def read(self):
    int_ = bytes_to_int(self.open_stream_in.read(math.ceil(self.width / 8)),
        self.width)
    self.repr_.setvalue(int_)
    return self.value.getvalue()
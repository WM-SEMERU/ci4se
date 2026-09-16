def to_ini(self):
    fake_io = io.StringIO()
    self.write(fake_io)
    return fake_io.getvalue()
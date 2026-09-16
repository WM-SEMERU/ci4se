def loads(self, s):
    io = six.StringIO()
    io.write(s)
    io.seek(0)
    self.load(io)
    self.validate()
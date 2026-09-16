def write(self, string, *args, **kwargs):
    if self.on_new_line:
        self.on_new_line = False
        if string.strip():
            self.indent()
    if args or kwargs:
        self.out_stream.write(string.format(*args, **kwargs))
    else:
        self.out_stream.write(string)
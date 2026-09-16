def compile(self):
    if self.buffer is None:
        self.buffer = self._compile_value(self.data, 0)
    return self.buffer.strip()
def write_padding(self, s):
    lines = s.splitlines(True)
    for line in lines:
        self.stream.write(line)
        if line[-1] in '\r\n':
            self._newline()
        else:
            self.generated_col += len(line)
def peek(self, n):
    pos = self._read_pos
    end = pos + n
    return self.raw[pos:end]
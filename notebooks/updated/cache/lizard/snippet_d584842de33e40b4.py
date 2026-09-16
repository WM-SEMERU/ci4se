def read(self, n=1):
    self.offset += n
    return self.data[self.offset - n:self.offset]
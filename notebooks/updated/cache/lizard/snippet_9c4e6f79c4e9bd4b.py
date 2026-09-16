def preamble(self, lenient=False):
    self.validate_signature()
    while True:
        if not self.atchunk:
            self.atchunk = self.chunklentype()
            if self.atchunk is None:
                raise FormatError('This PNG file has no IDAT chunks.')
        if self.atchunk[1] == 'IDAT':
            return
        self.process_chunk(lenient=lenient)
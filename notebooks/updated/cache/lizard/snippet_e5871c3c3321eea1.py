def disassemble(self, offset, size):
    for i in DCode(self.CM, offset, size, self.get_buff()[offset:offset + size]
        ).get_instructions():
        yield i
def read_code_bytes(self, size=128, offset=0):
    return self.get_process().read(self.get_pc() + offset, size)
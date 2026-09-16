def get(self, fmt, offset):
    bfo = BitFieldOperation(self.database, self.key)
    return bfo.get(fmt, offset)
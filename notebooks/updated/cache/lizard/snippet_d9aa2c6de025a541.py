def concat(self, operand, start=0, end=0, offset=0):
    if not Gauged.map_concat(self.ptr, operand.ptr, start, end, offset):
        raise MemoryError
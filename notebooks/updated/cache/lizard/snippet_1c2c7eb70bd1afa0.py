def encode(self, value):
    kassert.is_of_types(value, Bits)
    result = BitArray(value)
    result.reverse()
    return result
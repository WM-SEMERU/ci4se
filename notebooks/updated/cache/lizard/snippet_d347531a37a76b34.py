def zero_extend(self, new_length):
    si = self.copy()
    si._bits = new_length
    return si
def split_image(self, split_len):
    result = copy.copy(self)
    result.data = self.data[:split_len]
    self.data = self.data[split_len:]
    self.addr += split_len
    self.file_offs = None
    result.file_offs = None
    return result
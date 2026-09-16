def save_code(self, title, addr, _bytes):
    self.standard_bytes_header(title, addr, len(_bytes))
    _bytes = [self.BLOCK_TYPE_DATA] + [(int(x) & 255) for x in _bytes]
    self.standard_block(_bytes)
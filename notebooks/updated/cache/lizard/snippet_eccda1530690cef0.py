def read_utf(self, offset, len):
    try:
        result = self.data[offset:offset + len].decode('utf-8')
    except UnicodeDecodeError:
        result = str('')
    return result
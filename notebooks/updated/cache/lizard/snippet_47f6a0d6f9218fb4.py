def to_esc(self):
    chunks = chunked(self.stream, 2)
    return ''.join('\\x' + ''.join(pair) for pair in chunks)
def chunks(self, chunk_size=None):
    if not chunk_size:
        chunk_size = self.DEFAULT_CHUNK_SIZE
    try:
        self.seek(0)
    except (AttributeError, UnsupportedOperation):
        pass
    while True:
        data = self.read(chunk_size)
        if not data:
            break
        yield data
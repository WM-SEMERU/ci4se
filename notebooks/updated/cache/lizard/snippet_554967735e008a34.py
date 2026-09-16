def parse(self, data: bytes, context=None):
    stream = BytesIO(data)
    return self.parse_stream(stream, context)
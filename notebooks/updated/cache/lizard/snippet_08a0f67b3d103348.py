def write_stream(self, stream, validate=True):
    content = self.dump(validate=validate)
    try:
        if stream.seekable():
            stream.seek(0)
            stream.truncate(0)
        stream.write(content)
    except OSError as e:
        raise error.WriteError(e.errno)
def upload_from_stream(self, filename, source, chunk_size_bytes=None,
    metadata=None, session=None):
    with self.open_upload_stream(filename, chunk_size_bytes, metadata,
        session=session) as gin:
        gin.write(source)
    return gin._id
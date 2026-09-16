def stream_bytes(data, chunk_size=default_chunk_size):
    stream = BytesStream(data, chunk_size=chunk_size)
    return stream.body(), stream.headers
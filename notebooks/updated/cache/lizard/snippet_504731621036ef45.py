def stream_gzip_decompress_lines(stream):
    dec = zlib.decompressobj(zlib.MAX_WBITS | 16)
    previous = ''
    for compressed_chunk in stream:
        chunk = dec.decompress(compressed_chunk).decode()
        if chunk:
            lines = (previous + chunk).split('\n')
            previous = lines.pop()
            for line in lines:
                yield line
    yield previous
def from_offset(cls, chunk_type, stream_rdr, offset):
    px_width = stream_rdr.read_long(offset)
    px_height = stream_rdr.read_long(offset, 4)
    return cls(chunk_type, px_width, px_height)
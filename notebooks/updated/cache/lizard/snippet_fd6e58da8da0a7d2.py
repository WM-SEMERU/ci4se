def chunks(self, include_inactive=False):
    if include_inactive:
        chunk_count = sys.maxsize
    else:
        chunk_count = self.chunk_count()
    i = 0
    ofs = self._offset + self.header_chunk_size()
    while ofs + 65536 <= len(self._buf) and i < chunk_count:
        yield ChunkHeader(self._buf, ofs)
        ofs += 65536
        i += 1
def Initialize(self):
    super(AFF4ImageBase, self).Initialize()
    self.offset = 0
    self.chunk_cache = ChunkCache(self._WriteChunk, 100)
    if 'r' in self.mode:
        self.size = int(self.Get(self.Schema.SIZE))
        self.chunksize = int(self.Get(self.Schema._CHUNKSIZE))
        self.content_last = self.Get(self.Schema.CONTENT_LAST)
    else:
        self.size = 0
        self.content_last = None
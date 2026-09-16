def advance(self, blocksize):
    try:
        if self.increment_update_cache:
            self.update_cache_by_increment(blocksize)
        ts = DataBuffer.advance(self, blocksize)
        return self.check_valid(ts)
    except RuntimeError:
        self.null_advance(blocksize)
        return False
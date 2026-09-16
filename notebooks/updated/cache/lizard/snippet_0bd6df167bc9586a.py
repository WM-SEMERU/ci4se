def _ReadPartial(self, length):
    chunk = self.offset // self.chunksize
    chunk_offset = self.offset % self.chunksize
    available_to_read = min(length, self.chunksize - chunk_offset)
    retries = 0
    while retries < self.NUM_RETRIES:
        fd = self._GetChunkForReading(chunk)
        if fd:
            break
        logging.warning('Chunk not found.')
        time.sleep(1)
        retries += 1
    if retries >= self.NUM_RETRIES:
        raise IOError('Chunk not found for reading.')
    fd.seek(chunk_offset)
    result = fd.read(available_to_read)
    self.offset += len(result)
    return result
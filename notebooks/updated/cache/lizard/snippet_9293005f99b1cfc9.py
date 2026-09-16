def GetBlockHash(self, height):
    if self._current_block_height < height:
        return
    if len(self._header_index) <= height:
        return
    return self._header_index[height]
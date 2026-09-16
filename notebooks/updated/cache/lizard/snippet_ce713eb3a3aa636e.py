def _buffer_iter_rows(self, start):
    self._row_buffer = self[start:start + self._iter_row_buffer]
    self._row_buffer_index = 0
def read(self, n=-1):
    pos = self.tell()
    num_items_to_read = n if n != -1 else self.length - pos
    new_pos = min(pos + num_items_to_read, self.length)
    if new_pos > self._current_lob_length:
        missing_num_items_to_read = new_pos - self._current_lob_length
        self._read_missing_lob_data_from_db(self._current_lob_length,
            missing_num_items_to_read)
    self.seek(pos, SEEK_SET)
    return self.data.read(n)
def write_strand(self, strand):
    if strand['channel'
        ] != self._current_channel or self._strand_counter == self._reads_per_file:
        self._start_new_file(strand)
    fname = self._write_strand(strand)
    self._index.write('{}\t{}\t{}\t{}\n'.format(strand['channel'], strand[
        'read_attrs']['read_number'], self._current_file, fname))
    return
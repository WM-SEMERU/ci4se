def next(self, start):
    position = start
    while True:
        position = self._offset_of_next_ff_byte(start=position)
        position, byte_ = self._next_non_ff_byte(start=position + 1)
        if byte_ == b'\x00':
            continue
        marker_code, segment_offset = byte_, position + 1
        break
    return marker_code, segment_offset
def comparable(self):
    string_parts = []
    if self.location is not None:
        string_parts.append('location: {0:s}'.format(self.location))
    if self.part_index is not None:
        string_parts.append('part index: {0:d}'.format(self.part_index))
    if self.start_offset is not None:
        string_parts.append('start offset: 0x{0:08x}'.format(self.start_offset)
            )
    return self._GetComparable(sub_comparable_string=', '.join(string_parts))
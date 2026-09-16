def add_segment(self, address, data, overwrite=False):
    seg_type = self._classify_segment(address, len(data))
    if not isinstance(seg_type, DisjointSegment):
        raise ArgumentError('Unsupported segment type')
    segment = MemorySegment(address, address + len(data) - 1, len(data),
        bytearray(data))
    self._segments.append(segment)
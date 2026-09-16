def add_segment(self, segment):
    if self.segments:
        prev_seg = self.segments[-1]
        if (prev_seg.mode == segment.mode and prev_seg.encoding == segment.
            encoding):
            segment = _Segment(prev_seg.bits + segment.bits, prev_seg.
                char_count + segment.char_count, segment.mode, segment.encoding
                )
            self.bit_length -= len(prev_seg.bits)
            del self.segments[-1]
            del self.modes[-1]
    self.segments.append(segment)
    self.bit_length += len(segment.bits)
    self.modes.append(segment.mode)
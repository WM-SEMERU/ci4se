def save_segment(self, f, segment, checksum=None):
    segment_data = self.maybe_patch_segment_data(f, segment.data)
    f.write(struct.pack('<II', segment.addr, len(segment_data)))
    f.write(segment_data)
    if checksum is not None:
        return ESPLoader.checksum(segment_data, checksum)
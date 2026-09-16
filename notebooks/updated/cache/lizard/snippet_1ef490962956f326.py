def save_flash_segment(self, f, segment, checksum=None):
    segment_end_pos = f.tell() + len(segment.data) + self.SEG_HEADER_LEN
    segment_len_remainder = segment_end_pos % self.IROM_ALIGN
    if segment_len_remainder < 36:
        segment.data += b'\x00' * (36 - segment_len_remainder)
    return self.save_segment(f, segment, checksum)
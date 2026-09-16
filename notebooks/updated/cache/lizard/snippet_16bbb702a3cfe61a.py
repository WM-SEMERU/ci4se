def is_left_clip(self, cigar):
    left_tuple = cigar[0]
    right_tuple = cigar[-1]
    left_clipped = self.is_clip_op(left_tuple[0])
    right_clipped = self.is_clip_op(right_tuple[0])
    return (left_clipped and not right_clipped or left_clipped and
        right_clipped and left_tuple[1] > right_tuple[1])
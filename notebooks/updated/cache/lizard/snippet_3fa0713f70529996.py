def get_entire_style_ranges(self, split_comments=None, **kwargs):
    style_bits = self.get_style_bits(**kwargs)
    matches = self.get_comment_locations(**kwargs)
    groups = np.split(matches, np.where(np.diff(matches) != 0)[0] + 1)
    if split_comments is None:
        split_comments = []
    ranges = []
    last_end = 0
    if len(groups) == 1 and len(groups[0]) == 0:
        return
    last_style = -1
    for group in groups:
        size = len(group)
        next_end = last_end + size
        style = matches[last_end]
        masked_style = style & style_bits
        if style & comment_bit_mask:
            if masked_style in split_comments:
                ranges.append(((last_end, next_end), masked_style))
            elif last_style == masked_style:
                (prev_end, _), _ = ranges.pop()
                ranges.append(((prev_end, next_end), masked_style))
            else:
                ranges.append(((last_end, next_end), masked_style))
        elif last_style == masked_style:
            (prev_end, _), _ = ranges.pop()
            ranges.append(((prev_end, next_end), masked_style))
        else:
            ranges.append(((last_end, next_end), masked_style))
        last_style = masked_style
        last_end = next_end
    return ranges
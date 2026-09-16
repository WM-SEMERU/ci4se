def cal_position(self, text, has_toplinks, has_bottomlinks, head_len,
    head_start):
    if head_len == 0:
        top_start = top_end = bottom_start = bottom_end = 0
    else:
        top_start = top_end = head_start + 6
        bottom_start = bottom_end = head_start + head_len - 7
    if has_toplinks:
        t = r_top.search(text)
        if t:
            top_start, top_end = t.span()
    if has_bottomlinks:
        t = r_bottom.search(text)
        if t:
            bottom_start, bottom_end = t.span()
    return top_end, bottom_end
def find_row(self, ev_start, ev_end):
    all_starts = self.idx_annot_list.property('start')
    all_ends = self.idx_annot_list.property('end')
    for i, (start, end) in enumerate(zip(all_starts, all_ends)):
        if start == ev_start and end == ev_end:
            return i
    for i, start in enumerate(all_starts):
        if start == ev_start:
            return i
    for i, end in enumerate(all_ends):
        if end == ev_end:
            return i
    raise ValueError
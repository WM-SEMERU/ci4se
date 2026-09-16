def split(self, cutting_points, shift_times=False, overlap=0.0):
    if len(cutting_points) == 0:
        raise ValueError('At least one cutting-point is needed!')
    cutting_points = sorted(cutting_points)
    splits = []
    iv_start = 0.0
    for i in range(len(cutting_points) + 1):
        if i < len(cutting_points):
            iv_end = cutting_points[i]
        else:
            iv_end = float('inf')
        intervals = self.label_tree.overlap(iv_start - overlap, iv_end +
            overlap)
        cp_splits = LabelList(idx=self.idx)
        for iv in intervals:
            label = copy.deepcopy(iv.data)
            label.start = max(0, iv_start - overlap, label.start)
            label.end = min(iv_end + overlap, label.end)
            if shift_times:
                orig_start = max(0, iv_start - overlap)
                label.start -= orig_start
                label.end -= orig_start
            cp_splits.add(label)
        splits.append(cp_splits)
        iv_start = iv_end
    return splits
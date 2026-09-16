def target_range(self):
    a = self.alignment_ranges
    return GenomicRange(a[0][0].chr, a[0][0].start, a[-1][0].end)
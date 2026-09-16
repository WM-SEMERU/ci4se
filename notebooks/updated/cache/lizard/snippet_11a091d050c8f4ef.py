def add(self, start, end, val):
    insort(self.bins[bin_for_range(start, end, offsets=self.offsets)], (
        start, end, val))
    assert val >= 0
    self.max_val = max(self.max_val, val)
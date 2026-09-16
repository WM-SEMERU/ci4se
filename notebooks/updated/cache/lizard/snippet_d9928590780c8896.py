def as_fixed_width(self, copy=True):
    if self.bin_count == 0:
        raise RuntimeError('Cannot guess binning width with zero bins')
    elif self.bin_count == 1 or self.is_consecutive() and self.is_regular():
        return FixedWidthBinning(min=self.bins[0][0], bin_count=self.
            bin_count, bin_width=self.bins[1] - self.bins[0])
    else:
        raise RuntimeError(
            'Cannot create fixed-width binning from differing bin widths.')
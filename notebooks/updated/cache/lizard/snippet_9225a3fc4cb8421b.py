def containing_bins(start, stop=None):
    if stop is None:
        stop = start + 1
    max_bin = assign_bin(start, stop)
    return [bin for bin in overlapping_bins(start, stop) if bin <= max_bin]
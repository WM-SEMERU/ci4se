def window_boundaries(self, current_round):
    lo = max(0, current_round - self.window_length + 1)
    hi = current_round + 1
    return lo, hi
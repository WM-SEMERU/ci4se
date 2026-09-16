def get_bin_index(self, value):
    if value == self.max_value:
        return self.num_bins - 1
    return int(self.C * log(value / self.min_value))
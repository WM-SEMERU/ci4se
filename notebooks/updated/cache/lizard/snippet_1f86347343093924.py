def is_valid_interval(self, lower, upper):
    try:
        lower_idx = self.data.index(lower)
        upper_idx = self.data.index(upper)
        return (lower_idx, upper_idx) if lower_idx <= upper_idx else False
    except ValueError:
        return False
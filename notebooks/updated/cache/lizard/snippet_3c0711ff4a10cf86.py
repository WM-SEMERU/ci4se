def add_filter(self, new_filter, as_last=True):
    if as_last:
        self.filters.append(new_filter)
    else:
        self.filters = [new_filter] + self.filters
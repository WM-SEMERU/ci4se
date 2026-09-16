def dropna(self):
    not_nas = [v.notna() for v in self.values]
    and_filter = reduce(lambda x, y: x & y, not_nas)
    return self[and_filter]
def normalize_set(self, items, **kwargs):
    values = set()
    for item in ensure_list(items):
        values.update(self.normalize(item, **kwargs))
    return list(values)
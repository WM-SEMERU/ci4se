def add_filter(self, name, filter_values):
    if not isinstance(filter_values, (tuple, list)):
        if filter_values is None:
            return
        filter_values = [filter_values]
    self.filter_values[name] = filter_values
    f = self.facets[name].add_filter(filter_values)
    if f is None:
        return
    self._filters[name] = f
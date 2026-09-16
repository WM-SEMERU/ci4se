def add(self, title, values, **kwargs):
    if not is_list_like(values) and not isinstance(values, dict):
        values = [values]
    kwargs['title'] = title
    self.raw_series.append((values, kwargs))
    return self
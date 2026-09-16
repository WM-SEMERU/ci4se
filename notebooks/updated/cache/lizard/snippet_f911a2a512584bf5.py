def filter_params(self, value):
    if value is None:
        return {}
    val_min = value.get('min', None)
    val_max = value.get('max', None)
    params = {}
    if val_min == val_max:
        return {self.target: val_min}
    key = self.target + '__'
    if val_min is not None:
        params[key + self.lookup_types[0]] = val_min
    if val_max is not None:
        params[key + self.lookup_types[1]] = val_max
    return params
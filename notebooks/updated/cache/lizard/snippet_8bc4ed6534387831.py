def get(self, name=None, default=None):
    if name is None:
        return self.data
    if not isinstance(name, list):
        name = [name]
    data = self.data
    try:
        for key in name:
            data = data[key]
    except KeyError:
        return default
    return data
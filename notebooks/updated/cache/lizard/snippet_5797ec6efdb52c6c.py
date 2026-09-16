def get_data(self, compact=True):
    data = MultiDict()
    for field in self.fields:
        raw_value = field.from_python(self.python_data[field.name])
        field.set_raw_value(data, raw_value)
    if compact:
        data = MultiDict([(k, v) for k, v in data.items() if v])
    return data
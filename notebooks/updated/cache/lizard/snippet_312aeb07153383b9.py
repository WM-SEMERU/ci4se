def stringify_values(data):
    if not isinstance(data, dict):
        raise ValueError('Data must be dict. %r is passed' % data)
    values_dict = {}
    for key, value in data.items():
        items = []
        if isinstance(value, six.string_types):
            items.append(value)
        elif isinstance(value, Iterable):
            for v in value:
                if isinstance(v, int):
                    v = str(v)
                try:
                    item = six.u(v)
                except TypeError:
                    item = v
                items.append(item)
            value = ','.join(items)
        values_dict[key] = value
    return values_dict
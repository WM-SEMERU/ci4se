def juggle_types(data):
    if isinstance(data[0], list):
        return [[force_int(col) for col in row] for row in data]
    elif isinstance(data, list):
        return [force_int(i) for i in data]
    else:
        return data
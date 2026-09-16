def remove_none_value(data):
    return dict((k, v) for k, v in data.items() if v is not None)
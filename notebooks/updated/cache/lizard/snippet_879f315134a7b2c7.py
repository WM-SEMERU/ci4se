def save_list(key, *values):
    return json.dumps({key: [_get_json(value) for value in values]})
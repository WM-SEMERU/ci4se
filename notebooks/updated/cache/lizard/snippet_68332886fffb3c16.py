def get_dict_key(data, key):
    if isinstance(data, Mapping):
        if key in data:
            yield data[key]
        for key_data in data.values():
            for found in get_dict_key(key_data, key):
                yield found
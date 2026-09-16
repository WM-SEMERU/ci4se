def json_get(parsed_json, key):
    if key not in parsed_json:
        raise ValueError('JSON does not contain a {} field'.format(key))
    return parsed_json[key]
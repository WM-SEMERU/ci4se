def _convert_list_to_json(array):
    return json.dumps(array, skipkeys=False, allow_nan=False, indent=None,
        separators=(',', ':'))
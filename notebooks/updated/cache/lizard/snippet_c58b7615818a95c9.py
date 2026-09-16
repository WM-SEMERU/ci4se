def _convert_dict_to_json(array):
    return json.dumps(array, skipkeys=False, allow_nan=False, indent=None,
        separators=(',', ':'), sort_keys=True, default=lambda o: o.__dict__)
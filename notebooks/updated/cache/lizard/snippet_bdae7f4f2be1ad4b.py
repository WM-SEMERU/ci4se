def json_formatter(obj):
    if isinstance(obj, str):
        return json.dumps([obj], indent=True)
    else:
        return json.dumps(obj, indent=True, sort_keys=True)
def perform_import(val):
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item) for item in val]
    return val
def _serializeNT(data):
    if isinstance(data, list):
        return [_serializeNT(item) for item in data]
    elif isinstance(data, tuple) and hasattr(data, '_fields'):
        serialized = _serializeNT(dict(data._asdict()))
        serialized['__nt_name'] = data.__class__.__name__
        return serialized
    elif isinstance(data, tuple):
        return tuple(_serializeNT(item) for item in data)
    elif isinstance(data, dict):
        return {key: _serializeNT(data[key]) for key in data}
    return data
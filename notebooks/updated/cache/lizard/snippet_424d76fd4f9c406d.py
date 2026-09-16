def to_str(cls, values, callback=None):
    if callback and callable(callback):
        if isinstance(values, dict):
            return callback(_es.to_str(values))
        return [callback(_es.to_str(i)) for i in values]
    return _es.to_str(values)
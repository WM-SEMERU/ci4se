def _coerce_to_supported_type(cls, value):
    if value is None:
        return ''
    elif isinstance(value, dict):
        if '*' in value:
            return value['*']
        elif '__default__' in value:
            return value['__default__']
        else:
            return json.dumps(value, separators=(',', ':'))
    elif isinstance(value, bool):
        return value
    elif isinstance(value, float) or isinstance(value, int):
        return Decimal(value)
    else:
        return value
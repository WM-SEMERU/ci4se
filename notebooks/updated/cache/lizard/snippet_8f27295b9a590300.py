def serialize_for_header(key, value):
    if key in QUOTE_FIELDS:
        return json.dumps(value)
    elif isinstance(value, str):
        if ' ' in value or '\t' in value:
            return json.dumps(value)
        else:
            return value
    elif isinstance(value, list):
        return '[{}]'.format(', '.join(value))
    else:
        return str(value)
def _bytes_to_json(value):
    if isinstance(value, bytes):
        value = base64.standard_b64encode(value).decode('ascii')
    return value
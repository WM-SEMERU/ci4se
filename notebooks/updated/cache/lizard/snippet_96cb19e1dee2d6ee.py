def load(raw_bytes):
    try:
        if not isinstance(raw_bytes, string_type):
            raw_bytes = raw_bytes.decode()
        return json.loads(raw_bytes)
    except ValueError as e:
        raise SerializationException(str(e))
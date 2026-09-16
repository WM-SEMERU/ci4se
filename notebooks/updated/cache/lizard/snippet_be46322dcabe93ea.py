def is_iso8601(instance: str):
    if not isinstance(instance, str):
        return True
    return ISO8601.match(instance) is not None
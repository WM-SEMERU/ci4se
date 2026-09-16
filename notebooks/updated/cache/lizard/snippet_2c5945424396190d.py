def coerce(cls, key, value):
    if not isinstance(value, MutationDict):
        if isinstance(value, dict):
            return MutationDict(value)
        return Mutable.coerce(key, value)
    else:
        return value
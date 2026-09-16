def str(name, default=None, allow_none=False, fallback=None):
    value = read(name, default, allow_none, fallback=fallback)
    if value is None and allow_none:
        return None
    else:
        return builtins.str(value).strip()
def dict_pop_or(d, key, default=None):
    val = default
    with suppress(KeyError):
        val = d.pop(key)
    return val
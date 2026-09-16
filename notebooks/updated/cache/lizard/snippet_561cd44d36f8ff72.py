def coerce_to_list(val):
    if val:
        if not isinstance(val, (list, tuple)):
            val = [val]
    else:
        val = []
    return val
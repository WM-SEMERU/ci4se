def dict_values(src):
    for v in src.values():
        if isinstance(v, dict):
            for v in dict_values(v):
                yield v
        else:
            yield v
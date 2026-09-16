def to_int_list(values):
    results = []
    for v in values:
        try:
            results.append(int(v))
        except (TypeError, ValueError):
            results.append(0)
    return results
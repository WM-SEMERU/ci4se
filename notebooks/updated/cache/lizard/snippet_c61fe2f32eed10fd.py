def fill(xs, length, copy=False):
    if isinstance(xs, list) and len(xs) == length:
        return xs
    if length <= 0:
        return []
    try:
        xs = list(islice(xs, 0, length))
        if not xs:
            raise ValueError('empty input')
    except TypeError:
        xs = [xs]
    if len(xs) < length:
        if copy:
            last = xs[-1]
            xs.extend(deepcopy(last) for _ in range(length - len(xs)))
        else:
            xs.extend(islice(repeat(xs[-1]), 0, length - len(xs)))
    return xs
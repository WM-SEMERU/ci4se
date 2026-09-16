def parse_range_pairs(s, range_separator='-', convert_to_tuple=True):
    result = map(sorted, map(lambda r: (int(r.split(range_separator)[0]),
        int(r.split(range_separator)[1])) if range_separator in r else (int
        (r), int(r)), s.split(',')))
    if convert_to_tuple:
        return tuple(map(tuple, result))
    return result
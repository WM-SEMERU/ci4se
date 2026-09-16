def expand_region(tuple_of_s, a, b, start=0, stop=None):
    return tuple(expand_slice(s, a, b, start=start, stop=stop) for s in
        tuple_of_s)
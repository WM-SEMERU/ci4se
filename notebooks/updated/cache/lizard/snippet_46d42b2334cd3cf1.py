def _sec_to_str(t):
    from functools import reduce
    return '%d:%02d:%02d.%02d' % reduce(lambda ll, b: divmod(ll[0], b) + ll
        [1:], [(t * 100,), 100, 60, 60])
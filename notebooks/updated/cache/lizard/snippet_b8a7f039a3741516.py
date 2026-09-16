def subpaths_for_path_range(path_range, hardening_chars="'pH"):
    if path_range == '':
        yield ''
        return

    def range_iterator(the_range):
        for r in the_range.split(','):
            is_hardened = r[-1] in hardening_chars
            hardened_char = hardening_chars[-1] if is_hardened else ''
            if is_hardened:
                r = r[:-1]
            if '-' in r:
                low, high = [int(x) for x in r.split('-', 1)]
                for t in range(low, high + 1):
                    yield '%d%s' % (t, hardened_char)
            else:
                yield '%s%s' % (r, hardened_char)
    components = path_range.split('/')
    iterators = [range_iterator(c) for c in components]
    for v in itertools.product(*iterators):
        yield '/'.join(v)
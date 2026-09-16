def longest(*args):
    internal_assert(len(args) >= 2, 'longest expects at least two args')
    matcher = args[0] + skip_whitespace
    for elem in args[1:]:
        matcher ^= elem + skip_whitespace
    return matcher
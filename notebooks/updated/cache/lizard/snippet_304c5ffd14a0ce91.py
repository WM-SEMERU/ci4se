def _eratosthenes():
    d = {}
    for q in count(2):
        p = d.pop(q, None)
        if p is None:
            yield q
            d[q * q] = q
        else:
            x = p + q
            while x in d:
                x += p
            d[x] = p
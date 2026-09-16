def _to_binpoly(x):
    if x <= 0:
        return '0'
    b = 1
    c = []
    i = 0
    while x > 0:
        b = 1 << i
        if x & b:
            c.append(i)
            x ^= b
        i = i + 1
    return ' + '.join([('x^%i' % y) for y in c[::-1]])
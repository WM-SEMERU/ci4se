def window(ible, length):
    if length <= 0:
        raise ValueError
    ible = iter(ible)
    while True:
        elts = [xx for ii, xx in zip(range(length), ible)]
        if elts:
            yield elts
        else:
            break
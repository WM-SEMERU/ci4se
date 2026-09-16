def chunks(l, n):
    for i in _range(0, len(l), n):
        yield l[i:i + n]
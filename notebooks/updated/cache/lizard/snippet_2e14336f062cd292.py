def all_values(*values):
    print('here')
    values = [_normalize(v) for v in values]
    for v in zip(*values):
        yield all(v)
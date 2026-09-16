def from_mult_iters(cls, name=None, idx=None, **kwargs):
    if not name:
        name = 'table'
    lengths = [len(v) for v in kwargs.values()]
    if len(set(lengths)) != 1:
        raise ValueError('Iterables must all be same length')
    if not idx:
        raise ValueError('Must provide iter name index reference')
    index = kwargs.pop(idx)
    vega_vals = []
    for k, v in sorted(kwargs.items()):
        for idx, val in zip(index, v):
            value = {}
            value['idx'] = idx
            value['col'] = k
            value['val'] = val
            vega_vals.append(value)
    return cls(name, values=vega_vals)
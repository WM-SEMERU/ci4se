def merge(*tables, **kwargs):
    assert 'key' in kwargs, 'keyword argument "key" is required'
    key = kwargs['key']
    t1 = mergesort(*tables, **kwargs)
    t2 = mergeduplicates(t1, key=key, presorted=True)
    return t2
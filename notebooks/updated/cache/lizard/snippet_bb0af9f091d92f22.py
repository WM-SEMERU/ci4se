def ndim(n, *args, **kwargs):
    thunk = kwargs.get('thunk', lambda : random.random())
    if not args:
        return [thunk() for i in range(n)]
    A = []
    for i in range(n):
        A.append(ndim(*args, thunk=thunk))
    return A
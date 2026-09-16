def _op_factory(func, kwargs, opname, bands, rgb_op=False):

    def f(arr):
        newarr = arr.copy()
        if rgb_op:
            newarr[0:3] = func(newarr[0:3], **kwargs)
        else:
            for b in bands:
                newarr[b - 1] = func(arr[b - 1], **kwargs)
        return newarr
    f.__name__ = str(opname)
    return f
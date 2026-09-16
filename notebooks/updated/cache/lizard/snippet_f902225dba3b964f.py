def slice(ctx, x, start=None, stop=None, step=None, n_outputs=-1, outputs=None
    ):
    r
    import copy
    start = copy.copy(start)
    stop = copy.copy(stop)
    step = copy.copy(step)
    from .function_bases import slice as slice_base
    if start is None:
        start = (0,) * len(x.shape)
    if stop is None:
        stop = tuple(x.shape)
    if step is None:
        step = (1,) * len(x.shape)
    shape = x.shape
    for i, sss in enumerate(zip(start, stop, step)):
        s0, s1, s2 = sss
        SLICE_NONE = 2147483647
        if s0 == None:
            start[i] = SLICE_NONE
        if s1 == None:
            stop[i] = SLICE_NONE
        if s2 == None:
            step[i] = SLICE_NONE
    return slice_base(x, start, stop, step, n_outputs, outputs)
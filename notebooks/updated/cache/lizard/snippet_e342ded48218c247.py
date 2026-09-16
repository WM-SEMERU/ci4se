def unwrap(sig, max_delta=pi, step=2 * pi):
    idata = iter(sig)
    d0 = next(idata)
    yield d0
    delta = d0 - d0
    for d1 in idata:
        d_diff = d1 - d0
        if abs(d_diff) > max_delta:
            delta += -d_diff + min(d_diff % step, d_diff % -step, key=lambda
                x: abs(x))
        yield d1 + delta
        d0 = d1
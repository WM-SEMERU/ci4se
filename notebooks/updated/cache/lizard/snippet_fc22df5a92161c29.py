def windowed_run_events(da, window, dim='time'):
    d = rle(da, dim=dim)
    out = (d >= window).sum(dim=dim)
    return out
def windowed_run_count(da, window, dim='time'):
    d = rle(da, dim=dim)
    out = d.where(d >= window, 0).sum(dim=dim)
    return out
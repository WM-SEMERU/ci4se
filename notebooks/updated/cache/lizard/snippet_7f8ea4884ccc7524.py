def _pad_series(ts, pad, start, end):
    span = ts.span
    pada = max(int((span[0] - start) * ts.sample_rate.value), 0)
    padb = max(int((end - span[1]) * ts.sample_rate.value), 0)
    if pada or padb:
        return ts.pad((pada, padb), mode='constant', constant_values=(pad,))
    return ts
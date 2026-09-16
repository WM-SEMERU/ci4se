def get_closest_dt_padded_idx(dt, dt_list, pad=timedelta(days=30)):
    if not isinstance(pad, timedelta):
        pad = timedelta(days=pad)
    from pygeotools.lib import malib
    dt_list = malib.checkma(dt_list, fix=False)
    dt_diff = np.abs(dt - dt_list)
    valid_idx = (dt_diff.data < pad).nonzero()[0]
    return valid_idx
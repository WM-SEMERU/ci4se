def _amplitude_bounds(counts, bkg, model):
    if isinstance(counts, list):
        counts = np.concatenate([t.flat for t in counts])
        bkg = np.concatenate([t.flat for t in bkg])
        model = np.concatenate([t.flat for t in model])
    s_model = np.sum(model)
    s_counts = np.sum(counts)
    sn = bkg / model
    imin = np.argmin(sn)
    sn_min = sn[imin]
    c_min = counts[imin]
    b_min = c_min / s_model - sn_min
    b_max = s_counts / s_model - sn_min
    return max(b_min, 0), b_max
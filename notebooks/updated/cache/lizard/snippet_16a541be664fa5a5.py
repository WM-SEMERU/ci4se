def grid_bp_data(bps, items, mask=True):
    seen_ants = set()
    seen_pols = set()
    for ant1, ant2, pol in (bp_to_aap(bp) for bp in bps):
        seen_ants.add(ant1)
        seen_ants.add(ant2)
        seen_pols.add(pol)
    if len(seen_pols) != 2:
        raise Exception('can only work with 2 polarizations')
    pol1, pol2 = sorted(seen_pols)
    seen_ants = np.array(sorted(seen_ants))
    ant_map = dict((a, i) for i, a in enumerate(seen_ants))
    data = None
    n = len(seen_ants)
    for bp, value in items:
        if data is None:
            data = np.empty((n, n), dtype=np.result_type(value))
            data.fill(np.nan)
        ant1, ant2, pol = bp_to_aap(bp)
        i1 = ant_map[ant1]
        i2 = ant_map[ant2]
        if pol == pol1:
            data[i1, i2] = value
        else:
            data[i2, i1] = value
    if mask:
        data = np.ma.MaskedArray(data, ~np.isfinite(data))
    return pol1, pol2, seen_ants, data
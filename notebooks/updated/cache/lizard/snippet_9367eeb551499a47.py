def qtiling(fseries, qrange, frange, mismatch=0.2):
    qplane_tile_dict = {}
    qs = list(_iter_qs(qrange, deltam_f(mismatch)))
    for q in qs:
        qtilefreq = _iter_frequencies(q, frange, mismatch, fseries.duration)
        qplane_tile_dict[q] = numpy.array(list(qtilefreq))
    return qplane_tile_dict
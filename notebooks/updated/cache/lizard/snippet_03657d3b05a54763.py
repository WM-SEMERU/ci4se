def rogers_huff_r(gn):
    gn = asarray_ndim(gn, 2, dtype='i1')
    gn = memoryview_safe(gn)
    r = gn_pairwise_corrcoef_int8(gn)
    if r.size == 1:
        r = r[0]
    return r
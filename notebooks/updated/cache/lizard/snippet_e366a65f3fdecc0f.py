def cosmetics(flat1, flat2=None, mask=None, lowercut=6.0, uppercut=6.0,
    siglev=2.0):
    if flat2 is None:
        flat1, flat2 = flat2, flat1
        flat1 = numpy.ones_like(flat2)
    if type(mask) is not numpy.ndarray:
        mask = numpy.zeros(flat1.shape, dtype='int')
    ratio, mask = comp_ratio(flat1, flat2, mask)
    fratio1 = ratio[~mask]
    central = numpy.median(fratio1)
    std = robust_std(fratio1, central, siglev)
    mask_u = ratio > central + uppercut * std
    mask_d = ratio < central - lowercut * std
    mask_final = mask_u | mask_d | mask
    return mask_final
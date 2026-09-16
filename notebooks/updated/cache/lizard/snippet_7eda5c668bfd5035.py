def compute_hazard_maps(curves, imls, poes):
    poes = numpy.array(poes)
    if len(poes.shape) == 0:
        poes = poes.reshape(1)
    if len(curves.shape) == 1:
        curves = curves.reshape((1,) + curves.shape)
    L = curves.shape[1]
    if L != len(imls):
        raise ValueError('The curves have %d levels, %d were passed' % (L,
            len(imls)))
    result = []
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        imls = numpy.log(numpy.array(imls[::-1]))
    for curve in curves:
        curve_cutoff = [max(poe, EPSILON) for poe in curve[::-1]]
        hmap_val = []
        for poe in poes:
            if poe > curve_cutoff[-1]:
                hmap_val.append(0)
            else:
                val = numpy.exp(numpy.interp(numpy.log(poe), numpy.log(
                    curve_cutoff), imls))
                hmap_val.append(val)
        result.append(hmap_val)
    return numpy.array(result)
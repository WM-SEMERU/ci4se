def _stieltjes_analytical(dist, order, normed):
    dimensions = len(dist)
    mom_order = numpy.arange(order + 1).repeat(dimensions)
    mom_order = mom_order.reshape(order + 1, dimensions).T
    coeff1, coeff2 = dist.ttr(mom_order)
    coeff2[:, (0)] = 1.0
    poly = chaospy.poly.collection.core.variable(dimensions)
    if normed:
        orth = [poly ** 0 * numpy.ones(dimensions), (poly - coeff1[:, (0)]) /
            numpy.sqrt(coeff2[:, (1)])]
        for order_ in range(1, order):
            orth.append((orth[-1] * (poly - coeff1[:, (order_)]) - orth[-2] *
                numpy.sqrt(coeff2[:, (order_)])) / numpy.sqrt(coeff2[:, (
                order_ + 1)]))
        norms = numpy.ones(coeff2.shape)
    else:
        orth = [poly - poly, poly ** 0 * numpy.ones(dimensions)]
        for order_ in range(order):
            orth.append(orth[-1] * (poly - coeff1[:, (order_)]) - orth[-2] *
                coeff2[:, (order_)])
        orth = orth[1:]
        norms = numpy.cumprod(coeff2, 1)
    return orth, norms, coeff1, coeff2
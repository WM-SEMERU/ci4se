def insured_loss_curve(curve, deductible, insured_limit):
    losses, poes = curve[:, (curve[0] <= insured_limit)]
    limit_poe = interpolate.interp1d(*curve, bounds_error=False, fill_value=1)(
        deductible)
    return numpy.array([losses, numpy.piecewise(poes, [poes > limit_poe], [
        limit_poe, lambda x: x])])
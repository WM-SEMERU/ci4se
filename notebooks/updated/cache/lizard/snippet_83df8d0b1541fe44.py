def spectrum_to_xyz100(spectrum, observer):
    lambda_o, data_o = observer
    lambda_s, data_s = spectrum
    lmbda = numpy.sort(numpy.unique(numpy.concatenate([lambda_o, lambda_s])))
    assert lmbda[0] < 3.61e-07
    assert lmbda[-1] > 8.29e-07
    idata_o = numpy.array([numpy.interp(lmbda, lambda_o, dt) for dt in data_o])
    idata_s = numpy.interp(lmbda, lambda_s, data_s)
    delta = numpy.zeros(len(lmbda))
    diff = lmbda[1:] - lmbda[:-1]
    delta[1:] += diff
    delta[:-1] += diff
    delta /= 2
    values = numpy.dot(idata_o, idata_s * delta)
    return values * 100
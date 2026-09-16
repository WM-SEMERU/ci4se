def phase_shifted_coefficients(amplitude_coefficients, form='cos', shift=0.0):
    r
    if form != 'sin' and form != 'cos':
        raise NotImplementedError('Fourier series must have form sin or cos')
    A_0 = amplitude_coefficients[0]
    a_k = amplitude_coefficients[1::2]
    b_k = amplitude_coefficients[2::2]
    degree = a_k.size
    k = numpy.arange(1, degree + 1)
    A_k = numpy.sqrt(a_k ** 2 + b_k ** 2)
    if form == 'cos':
        Phi_k = numpy.arctan2(-a_k, b_k) + 2 * pi * k * shift
    elif form == 'sin':
        Phi_k = numpy.arctan2(b_k, a_k) + 2 * pi * k * shift
    Phi_k %= 2 * pi
    phase_shifted_coefficients_ = numpy.empty(amplitude_coefficients.shape,
        dtype=float)
    phase_shifted_coefficients_[0] = A_0
    phase_shifted_coefficients_[1::2] = A_k
    phase_shifted_coefficients_[2::2] = Phi_k
    return phase_shifted_coefficients_
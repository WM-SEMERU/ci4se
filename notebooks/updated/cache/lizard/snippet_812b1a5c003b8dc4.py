def SLIT_DIFFRACTION(x, g):
    y = zeros(len(x))
    index_zero = x == 0
    index_nonzero = ~index_zero
    dk_ = pi / g
    x_ = dk_ * x[index_nonzero]
    w_ = sin(x_)
    r_ = w_ ** 2 / x_ ** 2
    y[index_zero] = 1
    y[index_nonzero] = r_ / g
    return y
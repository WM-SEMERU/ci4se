def SpinTimes(spin, bias):
    if not isinstance(spin, int):
        raise TypeError('spin must be an int')
    if spin == -1:
        return Times(Real((-1, 1)), bias)
    elif spin == 1:
        return bias
    else:
        raise ValueError('expected spins to be -1., or 1.')
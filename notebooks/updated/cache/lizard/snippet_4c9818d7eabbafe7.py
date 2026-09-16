def define_noisy_readout(self, qubit, p00, p11):
    if not 0.0 <= p00 <= 1.0:
        raise ValueError('p00 must be in the interval [0,1].')
    if not 0.0 <= p11 <= 1.0:
        raise ValueError('p11 must be in the interval [0,1].')
    if not (isinstance(qubit, int) or isinstance(qubit, QubitPlaceholder)):
        raise TypeError(
            'qubit must be a non-negative integer, or QubitPlaceholder.')
    if isinstance(qubit, int) and qubit < 0:
        raise ValueError('qubit cannot be negative.')
    p00 = float(p00)
    p11 = float(p11)
    aprobs = [p00, 1.0 - p11, 1.0 - p00, p11]
    aprobs_str = '({})'.format(' '.join(format_parameter(p) for p in aprobs))
    pragma = Pragma('READOUT-POVM', [qubit], aprobs_str)
    return self.inst(pragma)
def from_zeros(self, lmax, kind='real', normalization='4pi', csphase=1):
    if kind.lower() not in ('real', 'complex'):
        raise ValueError("Kind must be 'real' or 'complex'. " +
            'Input value was {:s}.'.format(repr(kind)))
    if normalization.lower() not in ('4pi', 'ortho', 'schmidt', 'unnorm'):
        raise ValueError(
            "The normalization must be '4pi', 'ortho', 'schmidt', " +
            "or 'unnorm'. Input value was {:s}.".format(repr(normalization)))
    if csphase != 1 and csphase != -1:
        raise ValueError(
            'csphase must be either 1 or -1. Input value was {:s}.'.format(
            repr(csphase)))
    if normalization.lower() == 'unnorm' and lmax > 85:
        _warnings.warn('Calculations using unnormalized coefficients ' +
            'are stable only for degrees less than or equal ' +
            'to 85. lmax for the coefficients will be set to ' +
            '85. Input value was {:d}.'.format(lmax), category=RuntimeWarning)
        lmax = 85
    nl = lmax + 1
    if kind.lower() == 'real':
        coeffs = _np.zeros((2, nl, nl))
    else:
        coeffs = _np.zeros((2, nl, nl), dtype=complex)
    for cls in self.__subclasses__():
        if cls.istype(kind):
            return cls(coeffs, normalization=normalization.lower(), csphase
                =csphase)
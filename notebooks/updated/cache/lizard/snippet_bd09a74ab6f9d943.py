def from_zeros(self, lmax, gm, r0, omega=None, errors=False, normalization=
    '4pi', csphase=1):
    if normalization.lower() not in ('4pi', 'ortho', 'schmidt', 'unnorm'):
        raise ValueError(
            "The normalization must be '4pi', 'ortho', 'schmidt', or 'unnorm'. Input value was {:s}."
            .format(repr(normalization)))
    if csphase != 1 and csphase != -1:
        raise ValueError(
            'csphase must be either 1 or -1. Input value was {:s}.'.format(
            repr(csphase)))
    if normalization.lower() == 'unnorm' and lmax > 85:
        _warnings.warn(
            'Calculations using unnormalized coefficients are stable only for degrees less than or equal to 85. lmax for the coefficients will be set to 85. Input value was {:d}.'
            .format(lmax), category=RuntimeWarning)
        lmax = 85
    coeffs = _np.zeros((2, lmax + 1, lmax + 1))
    coeffs[0, 0, 0] = 1.0
    if errors is False:
        clm = SHGravRealCoeffs(coeffs, gm=gm, r0=r0, omega=omega,
            normalization=normalization.lower(), csphase=csphase)
    else:
        clm = SHGravRealCoeffs(coeffs, gm=gm, r0=r0, omega=omega, errors=
            _np.zeros((2, lmax + 1, lmax + 1)), normalization=normalization
            .lower(), csphase=csphase)
    return clm
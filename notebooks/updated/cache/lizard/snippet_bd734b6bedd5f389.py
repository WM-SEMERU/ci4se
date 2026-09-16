def SpinBasisKet(*numer_denom, hs):
    try:
        spin_numer, spin_denom = hs.spin.as_numer_denom()
    except AttributeError:
        raise TypeError(
            'hs=%s for SpinBasisKet must be a SpinSpace instance' % hs)
    assert spin_denom in (1, 2)
    if spin_denom == 1:
        if len(numer_denom) != 1:
            raise TypeError(
                'SpinBasisKet requires exactly one positional argument for an integer-spin Hilbert space'
                )
        numer = numer_denom[0]
        if numer < -spin_numer or numer > spin_numer:
            raise ValueError(
                'spin quantum number %s must be in range (%s, %s)' % (numer,
                -spin_numer, spin_numer))
        label = str(numer)
        if numer > 0:
            label = '+' + label
        return BasisKet(label, hs=hs)
    else:
        if len(numer_denom) != 2:
            raise TypeError(
                'SpinBasisKet requires exactly two positional arguments for a half-integer-spin Hilbert space'
                )
        numer, denom = numer_denom
        numer = int(numer)
        denom = int(denom)
        if denom != 2:
            raise ValueError(
                'The second positional argument (denominator of the spin quantum number) must be 2, not %s'
                 % denom)
        if numer < -spin_numer or numer > spin_numer:
            raise ValueError(
                'spin quantum number %s/%s must be in range (%s/2, %s/2)' %
                (numer, denom, -spin_numer, spin_numer))
        label = str(numer)
        if numer > 0:
            label = '+' + label
        label = label + '/2'
        return BasisKet(label, hs=hs)
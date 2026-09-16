def _expand(self, normalization, csphase, **kwargs):
    if normalization.lower() == '4pi':
        norm = 1
    elif normalization.lower() == 'schmidt':
        norm = 2
    elif normalization.lower() == 'unnorm':
        norm = 3
    elif normalization.lower() == 'ortho':
        norm = 4
    else:
        raise ValueError(
            "The normalization must be '4pi', 'ortho', 'schmidt', " +
            "or 'unnorm'. Input value was {:s}.".format(repr(normalization)))
    cilm = _shtools.SHExpandDH(self.data, norm=norm, csphase=csphase,
        sampling=self.sampling, **kwargs)
    coeffs = SHCoeffs.from_array(cilm, normalization=normalization.lower(),
        csphase=csphase, copy=False)
    return coeffs
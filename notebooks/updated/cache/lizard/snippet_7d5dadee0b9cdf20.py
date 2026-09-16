def to_array(self, itaper, normalization='4pi', csphase=1):
    if type(normalization) != str:
        raise ValueError('normalization must be a string. ' +
            'Input type was {:s}'.format(str(type(normalization))))
    if normalization.lower() not in ('4pi', 'ortho', 'schmidt'):
        raise ValueError("normalization must be '4pi', 'ortho' " +
            "or 'schmidt'. Provided value was {:s}".format(repr(normalization))
            )
    if csphase != 1 and csphase != -1:
        raise ValueError('csphase must be 1 or -1. Input value was {:s}'.
            format(repr(csphase)))
    return self._to_array(itaper, normalization=normalization.lower(),
        csphase=csphase)
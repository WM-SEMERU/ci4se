def concatenate(self, tpl, axis=None):
    if axis is None:
        raise NotImplementedError(
            'Sparse tensor concatenation without axis argument is not supported'
            )
    T = self
    for i in range(1, len(tpl)):
        T = _single_concatenate(T, tpl[i], axis=axis)
    return T
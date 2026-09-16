def shift(data, shift=(0, 0, 0), mode='constant', interpolation='linear'):
    if np.isscalar(shift):
        shift = (shift,) * 3
    if len(shift) != 3:
        raise ValueError('shift (%s) should be of length 3!')
    shift = -np.array(shift)
    return affine(data, mat4_translate(*shift), mode=mode, interpolation=
        interpolation)
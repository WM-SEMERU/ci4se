def pad_to_shape(d, dshape, mode='constant'):
    if d.shape == dshape:
        return d
    diff = np.array(dshape) - np.array(d.shape)
    slices = tuple(slice(-x // 2, x // 2) if x < 0 else slice(None, None) for
        x in diff)
    res = d[slices]
    return np.pad(res, [((int(np.ceil(d / 2.0)), d - int(np.ceil(d / 2.0))) if
        d > 0 else (0, 0)) for d in diff], mode=mode)
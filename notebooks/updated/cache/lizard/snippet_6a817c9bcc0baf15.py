def boundaries_to_intervals(boundaries):
    if not np.allclose(boundaries, np.unique(boundaries)):
        raise ValueError('Boundary times are not unique or not ascending.')
    intervals = np.asarray(list(zip(boundaries[:-1], boundaries[1:])))
    return intervals
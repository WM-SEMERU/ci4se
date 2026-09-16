def discr_sequence_space(shape, dtype=None, impl='numpy', **kwargs):
    shape = np.atleast_1d(shape)
    return uniform_discr([0] * len(shape), shape - 1, shape, dtype, impl,
        nodes_on_bdry=True, **kwargs)
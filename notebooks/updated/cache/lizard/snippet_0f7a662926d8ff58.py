def round_optimum(self, x):
    x = np.array(x)
    if not (x.ndim == 1 or x.ndim == 2 and x.shape[0] == 1):
        raise ValueError(
            'Unexpected dimentionality of x. Got {}, expected (1, N) or (N,)'
            .format(x.ndim))
    if x.ndim == 2:
        x = x[0]
    x_rounded = []
    value_index = 0
    for variable in self.space_expanded:
        var_value = x[value_index:value_index + variable.
            dimensionality_in_model]
        var_value_rounded = variable.round(var_value)
        x_rounded.append(var_value_rounded)
        value_index += variable.dimensionality_in_model
    return np.atleast_2d(np.concatenate(x_rounded))
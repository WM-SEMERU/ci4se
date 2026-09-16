def divide(self, phi1, inplace=True):
    phi = self if inplace else self.copy()
    phi1 = phi1.copy()
    if set(phi1.variables) - set(phi.variables):
        raise ValueError('Scope of divisor should be a subset of dividend')
    extra_vars = set(phi.variables) - set(phi1.variables)
    if extra_vars:
        slice_ = [slice(None)] * len(phi1.variables)
        slice_.extend([np.newaxis] * len(extra_vars))
        phi1.values = phi1.values[tuple(slice_)]
        phi1.variables.extend(extra_vars)
    for axis in range(phi.values.ndim):
        exchange_index = phi1.variables.index(phi.variables[axis])
        phi1.variables[axis], phi1.variables[exchange_index] = phi1.variables[
            exchange_index], phi1.variables[axis]
        phi1.values = phi1.values.swapaxes(axis, exchange_index)
    phi.values = phi.values / phi1.values
    phi.values[np.isnan(phi.values)] = 0
    if not inplace:
        return phi
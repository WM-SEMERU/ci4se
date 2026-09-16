def marginalize(self, variables, inplace=True):
    if not isinstance(variables, list):
        raise TypeError(
            'variables: Expected type list or array-like,got type {var_type}'
            .format(var_type=type(variables)))
    phi = self if inplace else self.copy()
    index_to_keep = [self.variables.index(var) for var in self.variables if
        var not in variables]
    phi.variables = [phi.variables[index] for index in index_to_keep]
    phi.mean = phi.mean[index_to_keep]
    phi.covariance = phi.covariance[np.ix_(index_to_keep, index_to_keep)]
    phi._precision_matrix = None
    if not inplace:
        return phi
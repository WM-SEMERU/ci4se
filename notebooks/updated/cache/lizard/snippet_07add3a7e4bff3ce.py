def reduce(self, values, inplace=True):
    if not isinstance(values, (list, tuple, np.ndarray)):
        raise TypeError('variables: Expected type: iterable, got: {var_type}'
            .format(var_type=type(values)))
    for var, value in values:
        if var not in self.variables:
            raise ValueError('{var} not in scope.'.format(var=var))
    phi = self if inplace else self.copy()
    var_to_remove = [var for var, value in values]
    var_to_keep = [var for var in self.variables if var not in var_to_remove]
    reduced_var_index = [(self.variables.index(var), value) for var, value in
        values]
    pdf = self.pdf

    def reduced_pdf(*args, **kwargs):
        reduced_args = list(args)
        reduced_kwargs = kwargs.copy()
        if reduced_args:
            for index, val in reduced_var_index:
                reduced_args.insert(index, val)
        if reduced_kwargs:
            for variable, val in values:
                reduced_kwargs[variable] = val
        if reduced_args and reduced_kwargs:
            reduced_args = [arg for arg in reduced_args if arg not in
                reduced_kwargs.values()]
        return pdf(*reduced_args, **reduced_kwargs)
    phi.variables = var_to_keep
    phi._pdf = reduced_pdf
    if not inplace:
        return phi
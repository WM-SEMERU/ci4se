def load_error(self):
    usecols = []
    for v in self.error_columns:
        if v is None:
            pass
        elif isinstance(v, int):
            usecols.append(v)
        elif len(v) is 2:
            for n in v:
                usecols.append(n)
    self.genfromtxt_args_error['usecols'] = tuple(usecols)
    array = numpy.genfromtxt(self.path, **self.genfromtxt_args_error)
    error = []
    for n, v in enumerate(self.error_columns):
        if v is None:
            error.append(None)
        elif isinstance(v, int):
            if len(usecols) is 1:
                error.append(array * self.scale[n])
            else:
                error.append(array[0] * self.scale[n])
                array = numpy.delete(array, 0, axis=0)
        elif len(v) is 2:
            error.append(array[0:2] * self.scale[n])
            array = numpy.delete(array, (0, 1), axis=0)
    return tuple(error)
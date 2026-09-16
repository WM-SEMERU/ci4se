def lmfit_parameter_values(self, params):
    return tuple(params[key].value for key in sorted(params))
def trim(self, lower=None, upper=None):
    if upper is None:
        upper = getattr(self.subpars.relwz, 'value', None)
    lland_parameters.ParameterSoil.trim(self, lower, upper)
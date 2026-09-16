def set_adapt_params(self, *args, **kwargs):
    r
    if args != ():
        raise TypeError(
            'keyword args only; try set_adapt_parameters(keyword = value)')
    self.covar_scale_multiplier = kwargs.pop('covar_scale_multiplier', self
        .covar_scale_multiplier)
    self.covar_scale_factor = kwargs.pop('covar_scale_factor', self.
        covar_scale_factor)
    self.covar_scale_factor_max = kwargs.pop('covar_scale_factor_max', self
        .covar_scale_factor_max)
    self.covar_scale_factor_min = kwargs.pop('covar_scale_factor_min', self
        .covar_scale_factor_min)
    self.force_acceptance_max = kwargs.pop('force_acceptance_max', self.
        force_acceptance_max)
    self.force_acceptance_min = kwargs.pop('force_acceptance_min', self.
        force_acceptance_min)
    self.damping = kwargs.pop('damping', self.damping)
    if not kwargs == {}:
        raise TypeError('unexpected keyword(s): ' + str(kwargs.keys()))
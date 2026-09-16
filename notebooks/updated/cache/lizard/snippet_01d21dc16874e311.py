def set_strategy(self, strategy, params=None):
    if not params:
        param_args = []
    elif isinstance(params, basestring):
        param_args = [str(p) for p in params.split(' ')]
    else:
        if not isinstance(params, collections.Iterable):
            params = params,
        param_args = [str(p) for p in params]
    samp_strategy = ' '.join([strategy] + param_args)
    return self._manager.set_sampling_strategy(self.name, samp_strategy)
def pso(self, n_particles, n_iterations, sigma_scale=1, print_key='PSO',
    threadCount=1):
    param_class = self._param_class
    init_pos = param_class.kwargs2args(self._lens_temp, self._source_temp,
        self._lens_light_temp, self._ps_temp, self._cosmo_temp)
    lens_sigma, source_sigma, lens_light_sigma, ps_sigma, cosmo_sigma = (self
        ._updateManager.sigma_kwargs)
    sigma_start = param_class.kwargs2args(lens_sigma, source_sigma,
        lens_light_sigma, ps_sigma, cosmo_sigma)
    lowerLimit = np.array(init_pos) - np.array(sigma_start) * sigma_scale
    upperLimit = np.array(init_pos) + np.array(sigma_start) * sigma_scale
    num_param, param_list = param_class.num_param()
    sampler = Sampler(likelihoodModule=self.likelihoodModule)
    result, chain = sampler.pso(n_particles, n_iterations, lowerLimit,
        upperLimit, init_pos=init_pos, threadCount=threadCount, mpi=self.
        _mpi, print_key=print_key)
    (lens_result, source_result, lens_light_result, ps_result, cosmo_result
        ) = param_class.args2kwargs(result, bijective=True)
    return (lens_result, source_result, lens_light_result, ps_result,
        cosmo_result, chain, param_list)
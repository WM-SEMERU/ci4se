def calculate_logevidence(cls, filename, thin_start=None, thin_end=None,
    thin_interval=None):
    with cls._io(filename, 'r') as fp:
        logls = fp.read_raw_samples(['loglikelihood'], thin_start=
            thin_start, thin_interval=thin_interval, thin_end=thin_end,
            temps='all', flatten=False)
        logls = logls['loglikelihood']
        betas = fp.betas
        ntemps = fp.ntemps
        nwalkers = fp.nwalkers
        ndim = len(fp.variable_params)
    dummy_sampler = emcee.PTSampler(ntemps, nwalkers, ndim, None, None,
        betas=betas)
    return dummy_sampler.thermodynamic_integration_log_evidence(logls=logls,
        fburnin=0.0)
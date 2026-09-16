def traptransit_MCMC(ts, fs, dfs=1e-05, nwalkers=200, nburn=300, niter=1000,
    threads=1, p0=[0.1, 0.1, 3, 0], return_sampler=False, maxslope=MAXSLOPE):
    model = TraptransitModel(ts, fs, dfs, maxslope=maxslope)
    sampler = emcee.EnsembleSampler(nwalkers, 4, model, threads=threads)
    T0 = p0[0] * (1 + rand.normal(size=nwalkers) * 0.1)
    d0 = p0[1] * (1 + rand.normal(size=nwalkers) * 0.1)
    slope0 = p0[2] * (1 + rand.normal(size=nwalkers) * 0.1)
    ep0 = p0[3] + rand.normal(size=nwalkers) * 0.0001
    p0 = np.array([T0, d0, slope0, ep0]).T
    pos, prob, state = sampler.run_mcmc(p0, nburn)
    sampler.reset()
    sampler.run_mcmc(pos, niter, rstate0=state)
    if return_sampler:
        return sampler
    else:
        return sampler.flatchain[:, (0)], sampler.flatchain[:, (1)
            ], sampler.flatchain[:, (2)], sampler.flatchain[:, (3)]
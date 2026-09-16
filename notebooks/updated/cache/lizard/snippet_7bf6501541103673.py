def cache_epsilons(dstore, oq, assetcol, riskmodel, E):
    if oq.ignore_covs or not riskmodel.covs:
        return
    A = len(assetcol)
    hdf5path = dstore.hdf5cache()
    logging.info('Storing the epsilon matrix in %s', hdf5path)
    if oq.calculation_mode == 'scenario_risk':
        eps = make_eps(assetcol.array, E, oq.master_seed, oq.asset_correlation)
    elif oq.asset_correlation:
        numpy.random.seed(oq.master_seed)
        eps = numpy.array([numpy.random.normal(size=E)] * A)
    else:
        seeds = oq.master_seed + numpy.arange(E)
        eps = numpy.zeros((A, E), F32)
        for i, seed in enumerate(seeds):
            numpy.random.seed(seed)
            eps[:, (i)] = numpy.random.normal(size=A)
    with hdf5.File(hdf5path) as cache:
        cache['epsilon_matrix'] = eps
    return hdf5path
def fit(model_code, *args, **kwargs):
    kwargs = dict(kwargs)
    kwargs['model_code'] = model_code
    if 'n_jobs' not in kwargs:
        kwargs['n_jobs'] = -1
    if model_code in FIT_CACHE:
        print('Reusing model.')
        kwargs['fit'] = FIT_CACHE[model_code]
    else:
        print('NOT reusing model.')
    start = time.time()
    FIT_CACHE[model_code] = pystan.stan(*args, **kwargs)
    print('Ran in %0.3f sec.' % (time.time() - start))
    return FIT_CACHE[model_code]
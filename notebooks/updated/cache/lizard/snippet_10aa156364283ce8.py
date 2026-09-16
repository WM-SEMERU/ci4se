def get_dummy_dynamic_run(nsamples, **kwargs):
    seed = kwargs.pop('seed', False)
    ndim = kwargs.pop('ndim', 2)
    nthread_init = kwargs.pop('nthread_init', 2)
    nthread_dyn = kwargs.pop('nthread_dyn', 3)
    logl_range = kwargs.pop('logl_range', 1)
    if kwargs:
        raise TypeError('Unexpected **kwargs: {0}'.format(kwargs))
    init = get_dummy_run(nthread_init, nsamples, ndim=ndim, seed=seed,
        logl_start=-np.inf, logl_range=logl_range)
    dyn_starts = list(np.random.choice(init['logl'], nthread_dyn, replace=True)
        )
    threads = nestcheck.ns_run_utils.get_run_threads(init)
    threads += [get_dummy_thread(nsamples, ndim=ndim, seed=False,
        logl_start=start, logl_range=logl_range) for start in dyn_starts]
    for i, _ in enumerate(threads):
        threads[i]['thread_labels'] = np.full(nsamples, i)
    run = nestcheck.ns_run_utils.combine_threads(threads)
    samples = nestcheck.write_polychord_output.run_dead_birth_array(run)
    return nestcheck.data_processing.process_samples_array(samples)
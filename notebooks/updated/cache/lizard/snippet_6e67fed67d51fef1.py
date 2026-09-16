def run_dead_birth_array(run, **kwargs):
    nestcheck.ns_run_utils.check_ns_run(run, **kwargs)
    threads = nestcheck.ns_run_utils.get_run_threads(run)
    samp_arrays = []
    ndim = run['theta'].shape[1]
    for th in threads:
        samp_arr = np.zeros((th['theta'].shape[0], ndim + 2))
        samp_arr[:, :ndim] = th['theta']
        samp_arr[:, (ndim)] = th['logl']
        samp_arr[1:, (ndim + 1)] = th['logl'][:-1]
        if th['thread_min_max'][0, 0] == -np.inf:
            samp_arr[0, ndim + 1] = -1e+30
        else:
            samp_arr[0, ndim + 1] = th['thread_min_max'][0, 0]
        samp_arrays.append(samp_arr)
    samples = np.vstack(samp_arrays)
    samples = samples[(np.argsort(samples[:, (ndim)])), :]
    return samples
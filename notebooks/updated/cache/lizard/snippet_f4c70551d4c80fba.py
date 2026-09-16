def _fluxes(sources, sinks, tprob, populations, for_committors=None):
    n_states = np.shape(populations)[0]
    if for_committors is None:
        for_committors = _committors(sources, sinks, tprob)
    else:
        for_committors = np.array(for_committors)
        if for_committors.shape != (n_states,):
            raise ValueError('Shape of committors %s should be %s' % (str(
                for_committors.shape), str((n_states,))))
    sources = np.array(sources).reshape((-1,))
    sinks = np.array(sinks).reshape((-1,))
    X = np.zeros((n_states, n_states))
    X[np.arange(n_states), np.arange(n_states)] = populations * (1.0 -
        for_committors)
    Y = np.zeros((n_states, n_states))
    Y[np.arange(n_states), np.arange(n_states)] = for_committors
    fluxes = np.dot(np.dot(X, tprob), Y)
    fluxes[np.arange(n_states), np.arange(n_states)] = np.zeros(n_states)
    return fluxes
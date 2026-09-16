def expand_variables_to_segments(v, Nt):
    N_v = len(np.atleast_1d(v[0]))
    return np.concatenate([np.full((Nt[i], N_v), v[i]) for i in np.arange(
        len(v))])
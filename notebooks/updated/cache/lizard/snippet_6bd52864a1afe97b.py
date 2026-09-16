def relaxation(P, p0, obs, times=[1], k=None, ncv=None):
    r
    M = P.shape[0]
    T = np.asarray(times).max()
    if T < M:
        return relaxation_matvec(P, p0, obs, times=times)
    else:
        return relaxation_decomp(P, p0, obs, times=times, k=k, ncv=ncv)
def profile_loglike(self, x):
    if self._prof_interp is None:
        return self._profile_loglike(x)[1]
    x = np.array(x, ndmin=1)
    return self._prof_interp(x)
def pericenter(self, return_times=False, func=np.mean, interp_kwargs=None,
    minimize_kwargs=None, approximate=False):
    if return_times and func is not None:
        raise ValueError(
            'Cannot return times if reducing pericenters using an input function. Pass `func=None` if you want to return all individual pericenters and times.'
            )
    if func is None:
        reduce = False
        func = lambda x: x
    else:
        reduce = True
    if self.t[-1] < self.t[0]:
        self = self[::-1]
    vals = []
    times = []
    for orbit in self.orbit_gen():
        v, t = orbit._max_helper(-orbit.physicsspherical.r, interp_kwargs=
            interp_kwargs, minimize_kwargs=minimize_kwargs, approximate=
            approximate)
        vals.append(func(-v))
        times.append(t)
    return self._max_return_helper(vals, times, return_times, reduce)
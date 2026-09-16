def scalefactor(self, other, qmin=None, qmax=None, Npoints=None):
    if qmin is None:
        qmin = max(self.q.min(), other.q.min())
    if qmax is None:
        xmax = min(self.q.max(), other.q.max())
    data1 = self.trim(qmin, qmax)
    data2 = other.trim(qmin, qmax)
    if Npoints is None:
        Npoints = min(len(data1), len(data2))
    commonx = np.linspace(max(data1.q.min(), data2.q.min()), min(data2.q.
        max(), data1.q.max()), Npoints)
    data1 = data1.interpolate(commonx)
    data2 = data2.interpolate(commonx)
    return nonlinear_odr(data1.Intensity, data2.Intensity, data1.Error,
        data2.Error, lambda x, a: a * x, [1])[0]
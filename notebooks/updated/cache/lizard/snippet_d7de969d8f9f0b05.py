def _call(self, x):
    y = self.data
    r = self.background
    obj = self.domain.zero()
    i = x.ufuncs.greater_equal(0)
    obj[i] = x[i] + r[i] - y[i]
    j = y.ufuncs.greater(0)
    k = i.ufuncs.logical_and(j)
    obj[k] += y[k] * (y[k] / (x[k] + r[k])).ufuncs.log()
    i = i.ufuncs.logical_not()
    obj[i] += y[i] / (2 * r[i] ** 2) * x[i] ** 2 + (1 - y[i] / r[i]) * x[i
        ] + r[i] - y[i]
    k = i.ufuncs.logical_and(j)
    obj[k] += y[k] * (y[k] / r[k]).ufuncs.log()
    return obj.inner(self.domain.one())
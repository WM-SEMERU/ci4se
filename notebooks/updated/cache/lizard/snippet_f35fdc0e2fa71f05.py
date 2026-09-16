def _derZ(self, x, y, z):
    m = len(x)
    temp = np.zeros((m, self.funcCount))
    for j in range(self.funcCount):
        temp[:, (j)] = self.functions[j](x, y, z)
    temp[np.isnan(temp)] = np.inf
    i = np.argmin(temp, axis=1)
    y = temp[np.arange(m), i]
    dfdz = np.zeros_like(x)
    for j in range(self.funcCount):
        c = i == j
        dfdz[c] = self.functions[j].derivativeZ(x[c], y[c], z[c])
    return dfdz
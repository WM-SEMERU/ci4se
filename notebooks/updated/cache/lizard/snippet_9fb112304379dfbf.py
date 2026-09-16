def run(self, d, x):
    N = len(x)
    if not len(d) == N:
        raise ValueError('The length of vector d and matrix x must agree.')
    self.n = len(x[0])
    try:
        x = np.array(x)
        d = np.array(d)
    except:
        raise ValueError('Impossible to convert x or d to a numpy array')
    y = np.zeros(N)
    e = np.zeros(N)
    self.w_history = np.zeros((N, self.n))
    for k in range(N):
        self.w_history[(k), :] = self.w
        y[k] = np.dot(self.w, x[k])
        e[k] = d[k] - y[k]
        R1 = np.dot(np.dot(np.dot(self.R, x[k]), x[k].T), self.R)
        R2 = self.mu + np.dot(np.dot(x[k], self.R), x[k].T)
        self.R = 1 / self.mu * (self.R - R1 / R2)
        dw = np.dot(self.R, x[k].T) * e[k]
        self.w += dw
    return y, e, self.w_history
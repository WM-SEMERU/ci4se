def inertia_tensor(self):
    mu = self.moments_central
    a = mu[0, 2]
    b = -mu[1, 1]
    c = mu[2, 0]
    return np.array([[a, b], [b, c]]) * u.pix ** 2
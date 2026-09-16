def _w_sigma_delta(self, sigma, delta):
    sigma2 = sigma ** 2
    w2 = sigma2 / (1 - 2 * delta ** 2 / np.pi)
    w = np.sqrt(w2)
    return w
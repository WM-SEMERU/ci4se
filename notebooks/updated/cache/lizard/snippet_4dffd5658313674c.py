def partial_derivative_mu(mu, sigma, low, high, data):
    pd_mu = np.sum(data - mu) / sigma ** 2
    pd_mu -= len(data) * ((norm.pdf(low, mu, sigma) - norm.pdf(high, mu,
        sigma)) / (norm.cdf(high, mu, sigma) - norm.cdf(low, mu, sigma)))
    return -pd_mu
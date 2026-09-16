def log_likelihood_rankings(data, params):
    loglik = 0
    params = np.asarray(params)
    for ranking in data:
        for i, winner in enumerate(ranking[:-1]):
            loglik -= logsumexp(params.take(ranking[i:]) - params[winner])
    return loglik
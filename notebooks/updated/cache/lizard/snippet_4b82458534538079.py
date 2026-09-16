def estimate_hmm(observations, nstates, lag=1, initial_model=None, output=
    None, reversible=True, stationary=False, p=None, accuracy=0.001, maxit=
    1000, maxit_P=100000, mincount_connectivity=0.01):
    r
    if output is None:
        output = _guess_output_type(observations)
    if lag > 1:
        observations = lag_observations(observations, lag)
    from bhmm.estimators.maximum_likelihood import MaximumLikelihoodEstimator as _MaximumLikelihoodEstimator
    est = _MaximumLikelihoodEstimator(observations, nstates, initial_model=
        initial_model, output=output, reversible=reversible, stationary=
        stationary, p=p, accuracy=accuracy, maxit=maxit, maxit_P=maxit_P)
    est.fit()
    est.hmm._lag = lag
    return est.hmm
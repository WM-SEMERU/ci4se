def bayesian_hmm(observations, estimated_hmm, nsample=100, reversible=True,
    stationary=False, p0_prior='mixed', transition_matrix_prior='mixed',
    store_hidden=False, call_back=None):
    r
    from bhmm.estimators.bayesian_sampling import BayesianHMMSampler as _BHMM
    sampler = _BHMM(observations, estimated_hmm.nstates, initial_model=
        estimated_hmm, reversible=reversible, stationary=stationary,
        transition_matrix_sampling_steps=1000, p0_prior=p0_prior,
        transition_matrix_prior=transition_matrix_prior, output=
        estimated_hmm.output_model.model_type)
    sampled_hmms = sampler.sample(nsamples=nsample,
        save_hidden_state_trajectory=store_hidden, call_back=call_back)
    from bhmm.hmm.generic_sampled_hmm import SampledHMM
    return SampledHMM(estimated_hmm, sampled_hmms)
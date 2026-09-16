def lp(**kwargs):
    obs_params = []
    syn_params, constraints = lp_syn(syn=False, **kwargs)
    obs_params += syn_params.to_list()
    return ParameterSet(obs_params), constraints
def _verify_names(sampler, var_names, arg_names):
    if hasattr(sampler, 'args'):
        num_vars = sampler.chain.shape[-1]
        num_args = len(sampler.args)
    elif hasattr(sampler, 'log_prob_fn'):
        num_vars = sampler.get_chain().shape[-1]
        num_args = len(sampler.log_prob_fn.args)
    else:
        num_vars = sampler.get_chain().shape[-1]
        num_args = 0
    if var_names is None:
        var_names = ['var_{}'.format(idx) for idx in range(num_vars)]
    if arg_names is None:
        arg_names = ['arg_{}'.format(idx) for idx in range(num_args)]
    if len(var_names) != num_vars:
        raise ValueError(
            'The sampler has {} variables, but only {} var_names were provided!'
            .format(num_vars, len(var_names)))
    if len(arg_names) != num_args:
        raise ValueError(
            'The sampler has {} args, but only {} arg_names were provided!'
            .format(num_args, len(arg_names)))
    return var_names, arg_names
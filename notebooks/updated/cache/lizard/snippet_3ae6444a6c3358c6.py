def _parse_hparams(hparams):
    prefixes = ['agent_', 'optimizer_', 'runner_', 'replay_buffer_']
    ret = []
    for prefix in prefixes:
        ret_dict = {}
        for key in hparams.values():
            if prefix in key:
                par_name = key[len(prefix):]
                ret_dict[par_name] = hparams.get(key)
        ret.append(ret_dict)
    return ret
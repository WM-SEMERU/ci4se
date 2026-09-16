def get(tgt, fun, tgt_type='glob', exclude_minion=False):
    if __opts__['file_client'] == 'local':
        ret = {}
        is_target = {'glob': __salt__['match.glob'], 'pcre': __salt__[
            'match.pcre'], 'list': __salt__['match.list'], 'grain':
            __salt__['match.grain'], 'grain_pcre': __salt__[
            'match.grain_pcre'], 'ipcidr': __salt__['match.ipcidr'],
            'compound': __salt__['match.compound'], 'pillar': __salt__[
            'match.pillar'], 'pillar_pcre': __salt__['match.pillar_pcre']}[
            tgt_type](tgt)
        if is_target:
            data = __salt__['data.get']('mine_cache')
            if isinstance(data, dict):
                if isinstance(fun, six.string_types):
                    functions = list(set(fun.split(',')))
                    _ret_dict = len(functions) > 1
                elif isinstance(fun, list):
                    functions = fun
                    _ret_dict = True
                else:
                    return {}
                if not _ret_dict and functions and functions[0] in data:
                    ret[__opts__['id']] = data.get(functions)
                elif _ret_dict:
                    for fun in functions:
                        if fun in data:
                            ret.setdefault(fun, {})[__opts__['id']] = data.get(
                                fun)
        return ret
    load = {'cmd': '_mine_get', 'id': __opts__['id'], 'tgt': tgt, 'fun':
        fun, 'tgt_type': tgt_type}
    ret = _mine_get(load, __opts__)
    if exclude_minion:
        if __opts__['id'] in ret:
            del ret[__opts__['id']]
    return ret
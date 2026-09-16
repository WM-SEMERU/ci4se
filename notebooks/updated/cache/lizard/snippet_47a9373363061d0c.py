def _cond_select_value_nonrecur(d, cond_match=None, **kwargs):
    if 'cond_func' in kwargs:
        cond_func = kwargs['cond_func']
    else:
        cond_func = _text_cond
    if 'cond_func_args' in kwargs:
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    rslt = {}
    for key in d:
        value = d[key]
        if cond_func(value, cond_match, *cond_func_args):
            rslt[key] = d[key]
        else:
            pass
    return rslt
def _prnt_min_max_val(var, text, verb):
    r
    if var.size > 3:
        print(text, _strvar(var.min()), '-', _strvar(var.max()), ':',
            _strvar(var.size), ' [min-max; #]')
        if verb > 3:
            print('                   : ', _strvar(var))
    else:
        print(text, _strvar(np.atleast_1d(var)))
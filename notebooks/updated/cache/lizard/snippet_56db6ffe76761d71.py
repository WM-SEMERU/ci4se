def calc_tr(calc_fn, *args, **kwargs):
    if not is_calc(calc_fn):
        calc_fn = calc(calc_fn)
    return calc_fn.tr(*args, **kwargs)
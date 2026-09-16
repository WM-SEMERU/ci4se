def _expand_delta(expr, idx):
    found_first_delta = False
    summands = None
    for factor in _factors_for_expand_delta(expr):
        need_to_expand = False
        if not found_first_delta and isinstance(factor, sympy.Basic):
            if factor.is_Add and _has_simple_delta(factor, idx):
                need_to_expand = True
        if need_to_expand:
            found_first_delta = True
            if summands is None:
                summands = list(factor.args)
            else:
                summands = [(summands[0] * t) for t in factor.args]
        elif summands is None:
            summands = [factor]
        else:
            summands = [(t * factor) for t in summands]
    return summands
def dropna(expr, how='any', thresh=None, subset=None):
    if subset is None:
        subset = [expr._get_field(c) for c in expr.schema.names]
    else:
        subset = [expr._get_field(c) for c in utils.to_list(subset)]
    if not subset:
        raise ValueError('Illegal subset is provided.')
    if thresh is None:
        thresh = len(subset) if how == 'any' else 1
    sum_exprs = reduce(operator.add, (s.notnull().ifelse(1, 0) for s in subset)
        )
    return expr.filter(sum_exprs >= thresh)
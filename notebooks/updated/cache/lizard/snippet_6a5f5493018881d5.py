def eval_formula(expr: str, dataframe=None, context=None):
    if context is None:
        dd = {}
    elif isinstance(context, CalibrationDict):
        dd = context.flat.copy()
    else:
        dd = context.copy()
    for k in [*dd.keys()]:
        dd[stringify_symbol(k)] = dd[k]
    expr_ast = parse_string(expr).value
    variables = list_variables(expr_ast)
    nexpr = stringify(expr_ast)
    dd['log'] = log
    dd['exp'] = exp
    if dataframe is not None:
        import pandas as pd
        for k, t in variables:
            dd[stringify_symbol((k, t))] = dataframe[k].shift(t)
        dd['t_'] = pd.Series(dataframe.index, index=dataframe.index)
    expr = to_source(nexpr)
    res = eval(expr, dd)
    return res
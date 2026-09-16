def infer_vegalite_type(data, ordinal_threshold=6):
    typ = pd_infer_dtype(data, **_infer_dtype_kwds)
    if typ in ('mixed-integer', 'integer'):
        if ordinal_threshold and pd.Series(data).nunique(
            ) <= ordinal_threshold:
            return 'ordinal'
        else:
            return 'quantitative'
    elif typ in ('floating', 'mixed-integer-float', 'complex'):
        return 'quantitative'
    elif typ in ('string', 'bytes', 'categorical', 'boolean', 'mixed',
        'unicode', 'object'):
        return 'nominal'
    elif typ in ('datetime', 'datetime64', 'timedelta', 'timedelta64',
        'date', 'time', 'period'):
        return 'temporal'
    else:
        warnings.warn(
            "I don't know how to infer vegalite type from '{0}'.  Defaulting to nominal."
            .format(typ))
        return 'nominal'
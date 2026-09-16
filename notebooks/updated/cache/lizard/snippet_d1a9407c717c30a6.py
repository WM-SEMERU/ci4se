def groupby(expr, by, *bys):
    if not isinstance(by, list):
        by = [by]
    if len(bys) > 0:
        by = by + list(bys)
    return GroupBy(_input=expr, _by=by)
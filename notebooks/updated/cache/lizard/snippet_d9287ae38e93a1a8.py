def _cellrepr(value, allow_formulas):
    if pd.isnull(value) is True:
        return ''
    if isinstance(value, float):
        value = repr(value)
    else:
        value = str(value)
    if not allow_formulas and value.startswith('='):
        value = "'%s" % value
    return value
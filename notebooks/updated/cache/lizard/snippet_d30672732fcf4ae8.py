def _process_generic_param(pval, def_unit, equivalencies=[]):
    if isinstance(pval, u.Quantity):
        outval = pval.to(def_unit, equivalencies).value
    else:
        outval = pval
    return outval
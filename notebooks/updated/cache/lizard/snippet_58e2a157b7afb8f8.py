def safe_cast(invar, totype):
    outvar = totype(invar)
    if not isinstance(outvar, totype):
        raise TypeError("Result of cast to '{0}' is '{1}'".format(totype,
            type(outvar)))
    return outvar
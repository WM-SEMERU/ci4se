def cfgGetBool(theObj, name, dflt):
    strval = theObj.get(name, None)
    if strval is None:
        return dflt
    return strval.lower().strip() == 'true'
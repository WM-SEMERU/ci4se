def saveVarsInMat(filename, varNamesStr, outOf=None, **opts):
    from mlabwrap import mlab
    filename, varnames, outOf = __saveVarsHelper(filename, varNamesStr,
        outOf, '.mat', **opts)
    try:
        for varname in varnames:
            mlab._set(varname, outOf[varname])
        mlab._do("save('%s','%s')" % (filename, "', '".join(varnames)), nout=0)
    finally:
        assert varnames
        mlab._do("clear('%s')" % "', '".join(varnames), nout=0)
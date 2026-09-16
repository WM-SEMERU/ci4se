def gfdist(target, abcorr, obsrvr, relate, refval, adjust, step, nintvls,
    cnfine, result=None):
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    if result is None:
        result = stypes.SPICEDOUBLE_CELL(2000)
    else:
        assert isinstance(result, stypes.SpiceCell)
        assert result.is_double()
    target = stypes.stringToCharP(target)
    abcorr = stypes.stringToCharP(abcorr)
    obsrvr = stypes.stringToCharP(obsrvr)
    relate = stypes.stringToCharP(relate)
    refval = ctypes.c_double(refval)
    adjust = ctypes.c_double(adjust)
    step = ctypes.c_double(step)
    nintvls = ctypes.c_int(nintvls)
    libspice.gfdist_c(target, abcorr, obsrvr, relate, refval, adjust, step,
        nintvls, ctypes.byref(cnfine), ctypes.byref(result))
    return result
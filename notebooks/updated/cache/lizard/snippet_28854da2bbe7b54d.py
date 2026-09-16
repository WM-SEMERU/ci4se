def gfrfov(inst, raydir, rframe, abcorr, obsrvr, step, cnfine, result=None):
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    if result is None:
        result = stypes.SPICEDOUBLE_CELL(2000)
    else:
        assert isinstance(result, stypes.SpiceCell)
        assert result.is_double()
    inst = stypes.stringToCharP(inst)
    raydir = stypes.toDoubleVector(raydir)
    rframe = stypes.stringToCharP(rframe)
    abcorr = stypes.stringToCharP(abcorr)
    obsrvr = stypes.stringToCharP(obsrvr)
    step = ctypes.c_double(step)
    libspice.gfrfov_c(inst, raydir, rframe, abcorr, obsrvr, step, ctypes.
        byref(cnfine), ctypes.byref(result))
    return result
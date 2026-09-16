def spkezr(targ, et, ref, abcorr, obs):
    targ = stypes.stringToCharP(targ)
    ref = stypes.stringToCharP(ref)
    abcorr = stypes.stringToCharP(abcorr)
    obs = stypes.stringToCharP(obs)
    starg = stypes.emptyDoubleVector(6)
    lt = ctypes.c_double()
    if hasattr(et, '__iter__'):
        states = []
        times = []
        for t in et:
            libspice.spkezr_c(targ, ctypes.c_double(t), ref, abcorr, obs,
                starg, ctypes.byref(lt))
            checkForSpiceError(None)
            states.append(stypes.cVectorToPython(starg))
            times.append(lt.value)
        return states, times
    else:
        libspice.spkezr_c(targ, ctypes.c_double(et), ref, abcorr, obs,
            starg, ctypes.byref(lt))
        return stypes.cVectorToPython(starg), lt.value
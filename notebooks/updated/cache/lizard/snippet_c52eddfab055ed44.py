def swpool(agent, nnames, lenvals, names):
    agent = stypes.stringToCharP(agent)
    nnames = ctypes.c_int(nnames)
    lenvals = ctypes.c_int(lenvals)
    names = stypes.listToCharArray(names)
    libspice.swpool_c(agent, nnames, lenvals, names)
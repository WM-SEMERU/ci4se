def Pcn(x, dsz, Nv, dimN=2, dimC=1, crp=False, zm=False):
    if crp:

        def zpadfn(x):
            return x
    else:

        def zpadfn(x):
            return zpad(x, Nv)
    if zm:

        def zmeanfn(x):
            return zeromean(x, dsz, dimN)
    else:

        def zmeanfn(x):
            return x
    return normalise(zmeanfn(zpadfn(bcrop(x, dsz, dimN))), dimN + dimC)
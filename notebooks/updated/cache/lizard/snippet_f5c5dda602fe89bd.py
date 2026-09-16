def pckfrm(pck, ids):
    pck = stypes.stringToCharP(pck)
    assert isinstance(ids, stypes.SpiceCell)
    assert ids.dtype == 2
    libspice.pckfrm_c(pck, ctypes.byref(ids))
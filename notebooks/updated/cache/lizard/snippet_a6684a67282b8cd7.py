def wnreld(a, op, b):
    assert isinstance(a, stypes.SpiceCell)
    assert b.dtype == 1
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == 1
    assert isinstance(op, str)
    op = stypes.stringToCharP(op.encode(encoding='UTF-8'))
    return bool(libspice.wnreld_c(ctypes.byref(a), op, ctypes.byref(b)))
def insrtd(item, inset):
    assert isinstance(inset, stypes.SpiceCell)
    if hasattr(item, '__iter__'):
        for d in item:
            libspice.insrtd_c(ctypes.c_double(d), ctypes.byref(inset))
    else:
        item = ctypes.c_double(item)
        libspice.insrtd_c(item, ctypes.byref(inset))
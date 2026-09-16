def is_np_compat():
    curr = ctypes.c_bool()
    check_call(_LIB.MXIsNumpyCompatible(ctypes.byref(curr)))
    return curr.value
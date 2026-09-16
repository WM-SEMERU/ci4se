def gfudb(udfuns, udfunb, step, cnfine, result):
    step = ctypes.c_double(step)
    libspice.gfudb_c(udfuns, udfunb, step, ctypes.byref(cnfine), ctypes.
        byref(result))
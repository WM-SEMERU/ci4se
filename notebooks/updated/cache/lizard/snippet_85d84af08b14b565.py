def serialise(structure):
    return ctypes.cast(ctypes.pointer(structure), ctypes.POINTER(ctypes.
        c_char * ctypes.sizeof(structure))).contents
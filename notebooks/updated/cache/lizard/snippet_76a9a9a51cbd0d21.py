def erract(op, lenout, action=None):
    if action is None:
        action = ''
    lenout = ctypes.c_int(lenout)
    op = stypes.stringToCharP(op)
    action = ctypes.create_string_buffer(str.encode(action), lenout.value)
    actionptr = ctypes.c_char_p(ctypes.addressof(action))
    libspice.erract_c(op, lenout, actionptr)
    return stypes.toPythonString(actionptr)
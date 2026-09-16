def et2lst(et, body, lon, typein, timlen=_default_len_out, ampmlen=
    _default_len_out):
    et = ctypes.c_double(et)
    body = ctypes.c_int(body)
    lon = ctypes.c_double(lon)
    typein = stypes.stringToCharP(typein)
    timlen = ctypes.c_int(timlen)
    ampmlen = ctypes.c_int(ampmlen)
    hr = ctypes.c_int()
    mn = ctypes.c_int()
    sc = ctypes.c_int()
    time = stypes.stringToCharP(timlen)
    ampm = stypes.stringToCharP(ampmlen)
    libspice.et2lst_c(et, body, lon, typein, timlen, ampmlen, ctypes.byref(
        hr), ctypes.byref(mn), ctypes.byref(sc), time, ampm)
    return hr.value, mn.value, sc.value, stypes.toPythonString(time
        ), stypes.toPythonString(ampm)
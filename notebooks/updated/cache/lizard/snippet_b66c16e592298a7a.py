def occult(target1, shape1, frame1, target2, shape2, frame2, abcorr,
    observer, et):
    target1 = stypes.stringToCharP(target1)
    shape1 = stypes.stringToCharP(shape1)
    frame1 = stypes.stringToCharP(frame1)
    target2 = stypes.stringToCharP(target2)
    shape2 = stypes.stringToCharP(shape2)
    frame2 = stypes.stringToCharP(frame2)
    abcorr = stypes.stringToCharP(abcorr)
    observer = stypes.stringToCharP(observer)
    et = ctypes.c_double(et)
    occult_code = ctypes.c_int()
    libspice.occult_c(target1, shape1, frame1, target2, shape2, frame2,
        abcorr, observer, et, ctypes.byref(occult_code))
    return occult_code.value
def libvlc_new(argc, argv):
    f = _Cfunctions.get('libvlc_new', None) or _Cfunction('libvlc_new', ((1
        ,), (1,)), class_result(Instance), ctypes.c_void_p, ctypes.c_int,
        ListPOINTER(ctypes.c_char_p))
    return f(argc, argv)
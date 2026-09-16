def set_info_handler(codec, handler, data=None):
    OPENJP2.opj_set_info_handler.argtypes = [CODEC_TYPE, ctypes.c_void_p,
        ctypes.c_void_p]
    OPENJP2.opj_set_info_handler.restype = check_error
    OPENJP2.opj_set_info_handler(codec, handler, data)
def destroy_codec(codec):
    OPENJP2.opj_destroy_codec.argtypes = [CODEC_TYPE]
    OPENJP2.opj_destroy_codec.restype = ctypes.c_void_p
    OPENJP2.opj_destroy_codec(codec)
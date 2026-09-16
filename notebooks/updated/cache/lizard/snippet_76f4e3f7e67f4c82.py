def encode(codec, stream):
    OPENJP2.opj_encode.argtypes = [CODEC_TYPE, STREAM_TYPE_P]
    OPENJP2.opj_encode.restype = check_error
    OPENJP2.opj_encode(codec, stream)
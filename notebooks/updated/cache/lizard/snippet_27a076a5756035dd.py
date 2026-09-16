def setup_decoder(codec, dparams):
    ARGTYPES = [CODEC_TYPE, ctypes.POINTER(DecompressionParametersType)]
    OPENJP2.opj_setup_decoder.argtypes = ARGTYPES
    OPENJP2.opj_setup_decoder.restype = check_error
    OPENJP2.opj_setup_decoder(codec, ctypes.byref(dparams))
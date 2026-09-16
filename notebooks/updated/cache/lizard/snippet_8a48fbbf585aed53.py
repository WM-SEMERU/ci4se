def pywt_pad_mode(pad_mode, pad_const=0):
    pad_mode = str(pad_mode).lower()
    if pad_mode == 'constant' and pad_const != 0.0:
        raise ValueError(
            'constant padding with constant != 0 not supported for `pywt` back-end'
            )
    try:
        return PAD_MODES_ODL2PYWT[pad_mode]
    except KeyError:
        raise ValueError("`pad_mode` '{}' not understood".format(pad_mode))
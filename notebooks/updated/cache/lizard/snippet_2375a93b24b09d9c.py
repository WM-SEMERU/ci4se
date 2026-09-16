def _parse_float_vec(vec):
    dtype = np.dtype('>u4,>u4')
    vec1 = vec.view(dtype=dtype)
    xport1 = vec1['f0']
    xport2 = vec1['f1']
    ieee1 = xport1 & 16777215
    shift = np.zeros(len(vec), dtype=np.uint8)
    shift[np.where(xport1 & 2097152)] = 1
    shift[np.where(xport1 & 4194304)] = 2
    shift[np.where(xport1 & 8388608)] = 3
    ieee1 >>= shift
    ieee2 = xport2 >> shift | (xport1 & 7) << 29 + (3 - shift)
    ieee1 &= 4293918719
    ieee1 |= ((xport1 >> 24 & 127) - 65 << 2
        ) + shift + 1023 << 20 | xport1 & 2147483648
    ieee = np.empty((len(ieee1),), dtype='>u4,>u4')
    ieee['f0'] = ieee1
    ieee['f1'] = ieee2
    ieee = ieee.view(dtype='>f8')
    ieee = ieee.astype('f8')
    return ieee
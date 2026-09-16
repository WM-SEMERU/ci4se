def _get_dtype_maps():
    tmp = [(np.float32, 'MET_FLOAT'), (np.float64, 'MET_DOUBLE'), (np.uint8,
        'MET_UCHAR'), (np.int8, 'MET_CHAR'), (np.uint16, 'MET_USHORT'), (np
        .int16, 'MET_SHORT'), (np.uint32, 'MET_UINT'), (np.int32, 'MET_INT'
        ), (np.uint64, 'MET_ULONG'), (np.int64, 'MET_LONG')]
    map1, map2 = {}, {}
    for np_type, itk_type in tmp:
        map1[np_type.__name__] = itk_type
        map2[itk_type] = np_type.__name__
    return map1, map2
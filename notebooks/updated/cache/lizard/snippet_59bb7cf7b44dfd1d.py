def native(data, format=segyio.SegySampleFormat.IBM_FLOAT_4_BYTE, copy=True):
    data = data.view(dtype=np.single)
    if copy:
        data = np.copy(data)
    format = int(segyio.SegySampleFormat(format))
    return segyio._segyio.native(data, format)
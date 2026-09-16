def qImageToArray(qimage, dtype='array'):
    result_shape = qimage.height(), qimage.width()
    temp_shape = qimage.height(), qimage.bytesPerLine() * 8 // qimage.depth()
    if qimage.format() in (QtGui.QImage.Format_ARGB32_Premultiplied, QtGui.
        QImage.Format_ARGB32, QtGui.QImage.Format_RGB32):
        if dtype == 'rec':
            dtype = np.dtype({'b': (np.uint8, 0), 'g': (np.uint8, 1), 'r':
                (np.uint8, 2), 'a': (np.uint8, 3)})
        elif dtype == 'array':
            dtype = np.uint8
            result_shape += 4,
            temp_shape += 4,
    elif qimage.format() == QtGui.QImage.Format_Indexed8:
        dtype = np.uint8
    else:
        raise ValueError('qimage2numpy only supports 32bit and 8bit images')
    buf = qimage.bits().asstring(qimage.byteCount())
    result = np.frombuffer(buf, dtype).reshape(temp_shape)
    if result_shape != temp_shape:
        result = result[:, :result_shape[1]]
    if qimage.format() == QtGui.QImage.Format_RGB32 and dtype == np.uint8:
        result = result[(...), :3]
        result = result[(...), ::-1]
    return result
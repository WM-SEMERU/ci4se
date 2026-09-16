def cudnnSetFilter4dDescriptor(wDesc, dataType, format, k, c, h, w):
    status = _libcudnn.cudnnSetFilter4dDescriptor(wDesc, dataType, format,
        k, c, h, w)
    cudnnCheckStatus(status)
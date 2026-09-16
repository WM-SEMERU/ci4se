def cudnnSetPooling2dDescriptor(poolingDesc, mode, windowHeight,
    windowWidth, verticalPadding, horizontalPadding, verticalStride,
    horizontalStride):
    status = _libcudnn.cudnnSetPooling2dDescriptor(poolingDesc, mode,
        windowHeight, windowWidth, verticalPadding, horizontalPadding,
        verticalStride, horizontalStride)
    cudnnCheckStatus(status)
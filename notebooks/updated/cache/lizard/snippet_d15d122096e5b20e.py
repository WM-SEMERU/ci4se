def pixelwise_or(self, binary_im):
    data = np.copy(self._data)
    ind = np.where(binary_im.data > 0)
    data[ind[0], ind[1], ...] = BINARY_IM_MAX_VAL
    return BinaryImage(data, self._frame)
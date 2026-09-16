def _image_data(self):
    return (self._data * (float(BINARY_IM_MAX_VAL) / MAX_IR)).astype(np.uint8)
def _load_into_numpy(sf, np_array, start, end, strides=None, shape=None):
    np_array[:] = 0.0
    np_array_2d = np_array.reshape((np_array.shape[0], np_array.shape[1] *
        np_array.shape[2]))
    _extensions.sframe_load_to_numpy(sf, np_array.ctypes.data, np_array_2d.
        strides, np_array_2d.shape, start, end)
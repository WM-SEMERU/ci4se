def _numpy_bytes_to_char(arr):
    arr = np.array(arr, copy=False, order='C', dtype=np.string_)
    return arr.reshape(arr.shape + (1,)).view('S1')
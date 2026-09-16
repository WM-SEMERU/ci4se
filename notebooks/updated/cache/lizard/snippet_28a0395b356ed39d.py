def axis_as_object(arr, axis=-1):
    shape = arr.shape
    arr = np.ascontiguousarray(np.rollaxis(arr, axis, arr.ndim))
    nbytes = arr.dtype.itemsize * shape[axis]
    voidtype = np.dtype((np.void, nbytes))
    return arr.view(voidtype).reshape(np.delete(shape, axis))
def unblockshaped(arr, h, w):
    n, nrows, ncols = arr.shape
    return arr.reshape(h // nrows, -1, nrows, ncols).swapaxes(1, 2).reshape(h,
        w)
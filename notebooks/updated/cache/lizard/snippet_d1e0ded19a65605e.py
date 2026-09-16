def as_square_array(arr):
    arr = np.atleast_2d(arr)
    if len(arr.shape) != 2 or arr.shape[0] != arr.shape[1]:
        raise ValueError('Expected square array')
    return arr
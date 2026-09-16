def total_variation(arr):
    return np.sum(np.abs(np.diff(arr, axis=0)), axis=0)
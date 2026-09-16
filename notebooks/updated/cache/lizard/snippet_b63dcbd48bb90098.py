def longest_run_1d(arr):
    v, rl = rle_1d(arr)[:2]
    return np.where(v, rl, 0).max()
def _replace_zeros(arr, default_min_value):
    min_nonzero_value = min(default_min_value, np.min(arr[arr > 0]))
    closest_to_zero = np.nextafter(min_nonzero_value, min_nonzero_value - 1)
    arr[arr == 0] = closest_to_zero
    return arr
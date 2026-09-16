def _diff_image(slice1, slice2, abs_value=True, cmap='gray', **kwargs):
    diff = slice1 - slice2
    if abs_value:
        diff = np.abs(diff)
    return diff, cmap
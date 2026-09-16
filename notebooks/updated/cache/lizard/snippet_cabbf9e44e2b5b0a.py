def calibrate_counts(array, attributes, index):
    offset = np.float32(attributes['corrected_counts_offsets'][index])
    scale = np.float32(attributes['corrected_counts_scales'][index])
    array = (array - offset) * scale
    return array
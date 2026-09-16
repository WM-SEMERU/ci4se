def calibrate_radiance(array, attributes, index):
    offset = np.float32(attributes['radiance_offsets'][index])
    scale = np.float32(attributes['radiance_scales'][index])
    array = (array - offset) * scale
    return array
def noise(params, amplitude=1, offset=0):
    amplitude = create_buffer(params, amplitude)
    offset = create_buffer(params, offset)
    output = offset + amplitude * (np.random.random(params.length) * 2 - 1)
    return output
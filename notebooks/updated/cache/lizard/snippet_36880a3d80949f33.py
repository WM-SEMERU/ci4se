def map2cube(data_map, layout):
    r
    if np.all(np.array(data_map.shape) % np.array(layout)):
        raise ValueError(
            'The desired layout must be a multiple of the number pixels in the data map.'
            )
    d_shape = np.array(data_map.shape) // np.array(layout)
    return np.array([data_map[slice(i * d_shape[0], (i + 1) * d_shape[0]),
        slice(j * d_shape[1], (j + 1) * d_shape[1])] for i in range(layout[
        0]) for j in range(layout[1])])
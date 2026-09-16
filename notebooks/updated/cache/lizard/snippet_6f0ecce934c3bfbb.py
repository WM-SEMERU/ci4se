def unit_vector(vector, **kwargs):
    vector = np.array(vector)
    out_shape = vector.shape
    vector = np.atleast_2d(vector)
    unit = vector / np.linalg.norm(vector, axis=1, **kwargs)[:, (None)]
    return unit.reshape(out_shape)
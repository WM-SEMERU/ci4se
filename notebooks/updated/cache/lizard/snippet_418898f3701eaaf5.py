def __f2d(frac_coords, v):
    return np.array([int(frac_coords[0] * v.shape[0]), int(frac_coords[1] *
        v.shape[1]), int(frac_coords[2] * v.shape[2])])
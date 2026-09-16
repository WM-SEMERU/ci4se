def vector_unit_nullrand(v, rng=None):
    if v.size == 0:
        return v
    mag = vector_mag(v)
    v_new = v.copy()
    v_new[mag == 0.0] = sphere_pick(v.shape[-1], (mag == 0.0).sum(), rng)
    v_new[mag > 0.0] /= mag[mag > 0.0][..., np.newaxis]
    return v_new
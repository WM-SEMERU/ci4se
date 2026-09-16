def ring_to_nested(ring_index, nside):
    nside = np.asarray(nside, dtype=np.intc)
    return _core.ring_to_nested(ring_index, nside)
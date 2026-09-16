def _confirm_constant(a):
    a = np.asanyarray(a)
    return np.isclose(a, 1.0).all(axis=0).any()
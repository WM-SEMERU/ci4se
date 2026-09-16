def _create_affine_features(output_shape, source_shape):
    ranges = [np.linspace(-1, 1, x, dtype=np.float32) for x in reversed(
        output_shape)]
    psi = [x.reshape(-1) for x in np.meshgrid(*ranges, indexing='xy')]
    dim_gap = len(source_shape) - len(output_shape)
    for _ in xrange(dim_gap):
        psi.append(np.zeros_like(psi[0], dtype=np.float32))
    psi.append(np.ones_like(psi[0], dtype=np.float32))
    return psi
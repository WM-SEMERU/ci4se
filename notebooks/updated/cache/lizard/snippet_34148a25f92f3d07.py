def morlet_filter_bank(samplerate, kernel_size, scale, scaling_factor,
    normalize=True):
    basis_size = len(scale)
    basis = np.zeros((basis_size, kernel_size), dtype=np.complex128)
    try:
        if len(scaling_factor) != len(scale):
            raise ValueError('scaling factor must have same length as scale')
    except TypeError:
        scaling_factor = np.repeat(float(scaling_factor), len(scale))
    sr = int(samplerate)
    for i, band in enumerate(scale):
        scaling = scaling_factor[i]
        w = band.center_frequency / (scaling * 2 * sr / kernel_size)
        basis[i] = morlet(M=kernel_size, w=w, s=scaling)
    basis = basis.real
    if normalize:
        basis /= np.linalg.norm(basis, axis=-1, keepdims=True) + 1e-08
    basis = ArrayWithUnits(basis, [FrequencyDimension(scale), TimeDimension
        (*samplerate)])
    return basis
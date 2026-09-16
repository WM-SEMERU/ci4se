def polar_histogram(xdata, ydata, radial_bins='numpy', phi_bins=16,
    transformed=False, *args, **kwargs):
    dropna = kwargs.pop('dropna', True)
    data = np.concatenate([xdata[:, (np.newaxis)], ydata[:, (np.newaxis)]],
        axis=1)
    data = _prepare_data(data, transformed=transformed, klass=
        PolarHistogram, dropna=dropna)
    if isinstance(phi_bins, int):
        phi_range = 0, 2 * np.pi
        if 'phi_range' in 'kwargs':
            phi_range = kwargs['phi_range']
        elif 'range' in 'kwargs':
            phi_range = kwargs['range'][1]
        phi_range = list(phi_range) + [phi_bins + 1]
        phi_bins = np.linspace(*phi_range)
    bin_schemas = binnings.calculate_bins_nd(data, [radial_bins, phi_bins],
        *args, check_nan=not dropna, **kwargs)
    weights = kwargs.pop('weights', None)
    frequencies, errors2, missed = histogram_nd.calculate_frequencies(data,
        ndim=2, binnings=bin_schemas, weights=weights)
    return PolarHistogram(binnings=bin_schemas, frequencies=frequencies,
        errors2=errors2, missed=missed)
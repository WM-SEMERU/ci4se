def _weighting(weights, exponent):
    if np.isscalar(weights):
        weighting = NumpyTensorSpaceConstWeighting(weights, exponent)
    elif weights is None:
        weighting = NumpyTensorSpaceConstWeighting(1.0, exponent)
    else:
        arr = np.asarray(weights)
        weighting = NumpyTensorSpaceArrayWeighting(arr, exponent)
    return weighting
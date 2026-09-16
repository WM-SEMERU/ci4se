def _mask_feature_data(feature_data, mask, mask_type):
    if mask_type.is_spatial() and feature_data.shape[1:3] != mask.shape[-3:-1]:
        raise ValueError(
            'Spatial dimensions of interpolation and mask feature do not match: {} {}'
            .format(feature_data.shape, mask.shape))
    if mask_type.is_time_dependent() and feature_data.shape[0] != mask.shape[0
        ]:
        raise ValueError(
            'Time dimension of interpolation and mask feature do not match: {} {}'
            .format(feature_data.shape, mask.shape))
    if mask.shape[-1] != feature_data.shape[-1]:
        mask = mask[..., 0]
    if mask_type is FeatureType.MASK:
        feature_data[mask, ...] = np.nan
    elif mask_type is FeatureType.MASK_TIMELESS:
        feature_data[:, (mask), (...)] = np.nan
    elif mask_type is FeatureType.LABEL:
        np.swapaxes(feature_data, 1, 3)
        feature_data[(mask), (...), :, :] = np.nan
        np.swapaxes(feature_data, 1, 3)
    return feature_data
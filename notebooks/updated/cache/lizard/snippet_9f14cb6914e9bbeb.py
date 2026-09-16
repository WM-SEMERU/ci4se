def transform_bbox(bbox, target_crs):
    warnings.warn(
        'This function is deprecated, use BBox.transform method instead',
        DeprecationWarning, stacklevel=2)
    return bbox.transform(target_crs)
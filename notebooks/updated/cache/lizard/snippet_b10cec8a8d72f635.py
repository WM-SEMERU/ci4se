def calc_anchors(preregistration_map, model, model_hemi, scale=1, sigma=
    Ellipsis, radius_weight=0, field_sign_weight=0, invert_rh_field_sign=False
    ):
    wgts = preregistration_map.prop('weight')
    rads = preregistration_map.prop('radius')
    if np.isclose(radius_weight, 0):
        radius_weight = 0
    ancs = retinotopy_anchors(preregistration_map, model, polar_angle=
        'polar_angle', eccentricity='eccentricity', radius='radius', weight
        =wgts, weight_min=0, radius_weight=radius_weight, field_sign_weight
        =field_sign_weight, scale=scale, invert_field_sign=model_hemi ==
        'rh' and invert_rh_field_sign, **{} if sigma is Ellipsis else {
        'sigma': sigma})
    return ancs
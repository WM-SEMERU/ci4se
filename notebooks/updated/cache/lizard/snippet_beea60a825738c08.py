def _scaled_bqm(bqm, scalar, bias_range, quadratic_range, ignored_variables,
    ignored_interactions, ignore_offset):
    bqm_copy = bqm.copy()
    if scalar is None:
        scalar = _calc_norm_coeff(bqm_copy.linear, bqm_copy.quadratic,
            bias_range, quadratic_range, ignored_variables,
            ignored_interactions)
    bqm_copy.scale(scalar, ignored_variables=ignored_variables,
        ignored_interactions=ignored_interactions, ignore_offset=ignore_offset)
    bqm_copy.info.update({'scalar': scalar})
    return bqm_copy
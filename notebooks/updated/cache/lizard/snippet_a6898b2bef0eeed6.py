def check_validity_of_long_form_args(model_obj, wide_weights, rows_to_obs):
    ensure_model_obj_has_mapping_constructor(model_obj)
    ensure_wide_weights_is_1D_or_2D_ndarray(wide_weights)
    ensure_rows_to_obs_validity(rows_to_obs)
    return None
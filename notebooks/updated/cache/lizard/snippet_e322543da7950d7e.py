def create_estimation_obj(model_obj, init_vals, mappings=None, ridge=None,
    constrained_pos=None, weights=None):
    mapping_matrices = model_obj.get_mappings_for_fit(
        ) if mappings is None else mappings
    zero_vector = np.zeros(init_vals.shape[0])
    internal_model_name = display_name_to_model_type[model_obj.model_type]
    estimator_class, current_split_func = model_type_to_resources[
        internal_model_name]['estimator'], model_type_to_resources[
        internal_model_name]['split_func']
    estimation_obj = estimator_class(model_obj, mapping_matrices, ridge,
        zero_vector, current_split_func, constrained_pos, weights=weights)
    return estimation_obj
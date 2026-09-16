def get_param_names(model_obj):
    all_names = deepcopy(model_obj.ind_var_names)
    if model_obj.intercept_names is not None:
        all_names = model_obj.intercept_names + all_names
    if model_obj.shape_names is not None:
        all_names = model_obj.shape_names + all_names
    if model_obj.nest_names is not None:
        all_names = model_obj.nest_names + all_names
    return all_names
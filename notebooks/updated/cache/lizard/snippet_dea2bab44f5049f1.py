def get_params_and_defaults(param_list, db):
    return [[p, d] for p, d in db.get_all_values_of_all_params().items()]
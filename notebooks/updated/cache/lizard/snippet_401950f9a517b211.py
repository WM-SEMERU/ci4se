def get_model_id_constraints(model):
    pkname = model.primary_key_name
    pkey = model.primary_key
    return get_id_constraints(pkname, pkey)
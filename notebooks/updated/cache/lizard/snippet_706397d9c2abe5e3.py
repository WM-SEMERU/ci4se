def _initialize_kvstore(kvstore, param_arrays, arg_params, param_names,
    update_on_kvstore):
    for idx, param_on_devs in enumerate(param_arrays):
        name = param_names[idx]
        kvstore.init(name, arg_params[name])
        if update_on_kvstore:
            kvstore.pull(name, param_on_devs, priority=-idx)
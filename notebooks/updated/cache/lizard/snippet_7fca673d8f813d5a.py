def get_parameters(signature, transmute_attrs, arguments_to_ignore=None):
    params = Parameters()
    used_keys = set(arguments_to_ignore or [])
    for key in ['query', 'header', 'path']:
        param_set = getattr(params, key)
        explicit_parameters = getattr(transmute_attrs, key + '_parameters')
        used_keys |= load_parameters(param_set, explicit_parameters,
            signature, transmute_attrs)
    body_parameters = transmute_attrs.body_parameters
    if isinstance(body_parameters, str):
        name = body_parameters
        params.body = Param(argument_name=name, description=transmute_attrs
            .parameter_descriptions.get(name), arginfo=signature.
            get_argument(name))
        used_keys.add(name)
    else:
        used_keys |= load_parameters(params.body, transmute_attrs.
            body_parameters, signature, transmute_attrs)
    for name in _extract_path_parameters_from_paths(transmute_attrs.paths):
        params.path[name] = Param(argument_name=name, description=
            transmute_attrs.parameter_descriptions.get(name), arginfo=
            signature.get_argument(name))
        used_keys.add(name)
    default_param_key = 'query' if transmute_attrs.methods == set(['GET']
        ) else 'body'
    default_params = getattr(params, default_param_key)
    for arginfo in signature:
        if arginfo.name in used_keys:
            continue
        used_keys.add(arginfo.name)
        default_params[arginfo.name] = Param(arginfo.name, description=
            transmute_attrs.parameter_descriptions.get(arginfo.name),
            arginfo=arginfo)
    return params
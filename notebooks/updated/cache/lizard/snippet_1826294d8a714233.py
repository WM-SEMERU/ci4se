def parameters_from_model(parameters_model):
    parameters = {}
    for p in parameters_model:
        if p.is_function:
            code, defaults, closure = pickle.loads(p.value)
            parameters[p.key] = func_load(code, defaults, closure, globs=
                globals())
        elif p.is_set:
            parameters[p.key] = set(p.value)
        else:
            parameters[p.key] = p.value
    return parameters
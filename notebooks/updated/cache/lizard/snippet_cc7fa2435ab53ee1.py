def create(parameter_names, parameter_types, return_type):
    ordered_pairs = [(name, parameter_types[name]) for name in parameter_names]
    return MethodSignature(ordered_pairs, return_type)
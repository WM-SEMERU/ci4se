def check_types(parameters, parameter_types, strict_floats):
    for name, parameter_type in parameter_types.items():
        if name not in parameters:
            raise InvalidParamsError("Parameter '{}' is missing.".format(name))
        if not _is_instance(parameters[name], parameter_type, strict_floats):
            raise InvalidParamsError(
                "Value '{}' for parameter '{}' is not of expected type {}."
                .format(parameters[name], name, parameter_type))
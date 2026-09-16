def parse_signature(cls, function):
    annotations = function.__annotations__.copy()
    del annotations['return']
    result = []
    for param_name, (param_type, param_obj) in annotations.items():
        sig_param = function.signature.parameters[param_name]
        param_description = {'paramType': param_type, 'name': param_name,
            'required': sig_param.default is inspect.Parameter.empty}
        param_description.update(param_obj.describe())
        result.append(param_description)
    return result
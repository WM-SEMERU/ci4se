def header_param(name, required=False, param_type='string'):
    return swagger.HeaderParameterSubSchema(**{'name': name, 'in': 'header',
        'required': required, 'type': param_type})
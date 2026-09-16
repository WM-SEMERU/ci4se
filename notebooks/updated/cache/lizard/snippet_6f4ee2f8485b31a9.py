def parse_signature(signature):
    if ' -> ' not in signature:
        param_types, return_type = None, signature.strip()
    else:
        lhs, return_type = [s.strip() for s in signature.split(' -> ')]
        csv = lhs[1:-1].strip()
        param_types = split_parameter_types(csv)
    requires = set(_RE_QUALIFIED_TYPES.findall(signature))
    return param_types, return_type, requires
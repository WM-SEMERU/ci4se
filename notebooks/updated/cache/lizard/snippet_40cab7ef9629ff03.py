def _from_safe_path_param_name(safe_parameter):
    assert safe_parameter.startswith('_')
    safe_parameter_as_base32 = safe_parameter[1:]
    padding_length = -len(safe_parameter_as_base32) % 8
    padding = '=' * padding_length
    return base64.b32decode(safe_parameter_as_base32 + padding)
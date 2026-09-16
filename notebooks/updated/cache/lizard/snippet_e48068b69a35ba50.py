def _error_code_to_str(mod, type_, code):
    _, c_name = _get_error_names(mod, type_, code)
    return '%s(%d)' % (c_name, code)
def _find_assignment(arg_token):
    idx = arg_token.find('=')
    while idx != -1:
        if idx != 0 and arg_token[idx - 1] != '\\':
            return idx
        idx = arg_token.find('=', idx + 1)
    return -1
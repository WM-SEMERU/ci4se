def create_result(self, env_name, other_val, meta, val, dividers):
    args = [env_name]
    if other_val is NotSpecified:
        other_val = None
    if not dividers:
        args.extend([None, None])
    elif dividers[0] == ':':
        args.extend([other_val, None])
    elif dividers[0] == '=':
        args.extend([None, other_val])
    return Environment(*args)
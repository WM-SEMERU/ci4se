def convertstatsmethod(method_str):
    if StringClass.string_match(method_str, 'Average'):
        return 'ave'
    elif StringClass.string_match(method_str, 'Maximum'):
        return 'max'
    elif StringClass.string_match(method_str, 'Minimum'):
        return 'min'
    elif method_str.lower() in ['ave', 'max', 'min']:
        return method_str.lower()
    else:
        return 'ave'
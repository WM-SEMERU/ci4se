def remove_cv(type_):
    nake_type = remove_alias(type_)
    if not is_const(nake_type) and not is_volatile(nake_type):
        return type_
    result = nake_type
    if is_const(result):
        result = remove_const(result)
    if is_volatile(result):
        result = remove_volatile(result)
    if is_const(result):
        result = remove_const(result)
    return result
def var_contains(var, value):
    setval = get_var(var)
    value = value.replace('\\', '')
    if setval is None:
        return False
    return value in setval.split()
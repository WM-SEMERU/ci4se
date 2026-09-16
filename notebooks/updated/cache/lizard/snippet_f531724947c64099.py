def pluralize(singular=None):
    if singular.endswith('y') and not singular.endswith('ay'):
        plural = singular[:-1] + 'ies'
    elif singular.endswith('s'):
        plural = singular + 'es'
    else:
        plural = singular + 's'
    return plural
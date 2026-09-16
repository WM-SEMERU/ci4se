def params_for(prefix, kwargs):
    if not prefix.endswith('__'):
        prefix += '__'
    return {key[len(prefix):]: val for key, val in kwargs.items() if key.
        startswith(prefix)}
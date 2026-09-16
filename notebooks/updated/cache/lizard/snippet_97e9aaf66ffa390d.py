def collect(cls):
    constants = {}
    for method_path in WebpackConstants.get_constant_processors():
        method = import_string(method_path)
        if not callable(method):
            raise ImproperlyConfigured(
                'Constant processor "%s" is not callable' % method_path)
        result = method(constants)
        if isinstance(result, dict):
            constants.update(result)
    return constants
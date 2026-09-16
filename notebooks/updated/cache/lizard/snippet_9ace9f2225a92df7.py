def apply_reform(self, reform_path):
    from openfisca_core.reforms import Reform
    try:
        reform_package, reform_name = reform_path.rsplit('.', 1)
    except ValueError:
        raise ValueError(
            '`{}` does not seem to be a path pointing to a reform. A path looks like `some_country_package.reforms.some_reform.`'
            .format(reform_path))
    try:
        reform_module = importlib.import_module(reform_package)
    except ImportError:
        message = linesep.join([traceback.format_exc(),
            'Could not import `{}`.'.format(reform_package),
            'Are you sure of this reform module name? If so, look at the stack trace above to determine the origin of this error.'
            ])
        raise ValueError(message)
    reform = getattr(reform_module, reform_name, None)
    if reform is None:
        raise ValueError('{} has no attribute {}'.format(reform_package,
            reform_name))
    if not issubclass(reform, Reform):
        raise ValueError('`{}` does not seem to be a valid Openfisca reform.'
            .format(reform_path))
    return reform(self)
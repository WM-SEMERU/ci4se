def _defaultErrorHandler(varBinds, **context):
    errors = context.get('errors')
    if errors:
        err = errors[-1]
        raise err['error']
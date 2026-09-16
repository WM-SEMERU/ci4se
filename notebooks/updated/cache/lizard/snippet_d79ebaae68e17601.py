def _compile_scalar(schema):
    if inspect.isclass(schema):

        def validate_instance(path, data):
            if isinstance(data, schema):
                return data
            else:
                msg = 'expected %s' % schema.__name__
                raise er.TypeInvalid(msg, path)
        return validate_instance
    if callable(schema):

        def validate_callable(path, data):
            try:
                return schema(data)
            except ValueError as e:
                raise er.ValueInvalid('not a valid value', path)
            except er.Invalid as e:
                e.prepend(path)
                raise
        return validate_callable

    def validate_value(path, data):
        if data != schema:
            raise er.ScalarInvalid('not a valid value', path)
        return data
    return validate_value
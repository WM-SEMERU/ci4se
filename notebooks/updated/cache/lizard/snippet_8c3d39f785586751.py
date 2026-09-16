def optional(_object):
    if is_callable(_object):
        validator = _object

        @wraps(validator)
        def decorated(value):
            if value:
                return validator(value)
            return
        return decorated
    else:

        def optional(*args):
            return _object
        optional.is_optional = True
        optional._object = _object
        return optional
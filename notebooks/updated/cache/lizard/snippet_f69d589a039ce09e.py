def without_property_validation(input_function):

    @wraps(input_function)
    def func(*args, **kwargs):
        with validate(False):
            return input_function(*args, **kwargs)
    return func
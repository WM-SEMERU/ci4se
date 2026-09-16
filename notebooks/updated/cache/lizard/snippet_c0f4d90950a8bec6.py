def capability(cap, *wrap_exceptions):
    if isinstance(cap, WNetworkClientCapabilities) is True:
        cap = cap.value
    elif isinstance(cap, str) is False:
        raise TypeError('Invalid capability type')

    def first_level_decorator(decorated_function):

        def second_level_decorator(original_function, *args, **kwargs):
            if len(wrap_exceptions) == 0:
                return original_function(*args, **kwargs)
            try:
                return original_function(*args, **kwargs)
            except wrap_exceptions as e:
                raise WClientCapabilityError(
                    'Error during "%s" capability execution' % cap) from e
        result_fn = decorator(second_level_decorator)(decorated_function)
        result_fn.__capability_name__ = cap
        return result_fn
    return first_level_decorator
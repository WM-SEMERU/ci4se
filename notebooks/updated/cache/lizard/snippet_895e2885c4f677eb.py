def accept_quantity(input_type=float, allow_none=False):

    def accept_quantity_wrapper(method):

        def handle_quantity(instance, value, *args, **kwargs):
            try:
                new_value = input_type(value)
                return method(instance, new_value, *args, **kwargs)
            except TypeError:
                if isinstance(value, u.Quantity):
                    new_value = value.to(instance.unit).value
                    return method(instance, new_value, *args, **kwargs)
                elif value is None:
                    if allow_none:
                        return method(instance, None, *args, **kwargs)
                    else:
                        raise TypeError(
                            'You cannot pass None as argument for method %s of %s'
                             % (method.__name__, instance.name))
                else:
                    raise TypeError(
                        'You need to pass either a %s or a astropy.Quantity to method %s of %s'
                         % (input_type.__name__, method.__name__, instance.
                        name))
        return handle_quantity
    return accept_quantity_wrapper
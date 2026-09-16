def send_periodic(bus, message, period, *args, **kwargs):
    warnings.warn(
        'The function `can.send_periodic` is deprecated and will ' +
        'be removed in an upcoming version. Please use `can.Bus.send_periodic` instead.'
        , DeprecationWarning)
    return bus.send_periodic(message, period, *args, **kwargs)
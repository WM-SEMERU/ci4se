def _xray_register_type_fix(wrapped, instance, args, kwargs):
    our_args = list(copy.copy(args))
    if len(our_args) == 2 and isinstance(our_args[1], (XRayTracedConn,
        XRayTracedCursor)):
        our_args[1] = our_args[1].__wrapped__
    return wrapped(*our_args, **kwargs)
def _get_handler_set(cls, request, fail_enum, header_proto=None):
    added = set()
    handlers = []
    for controls in request.sorting:
        control_bytes = controls.SerializeToString()
        if control_bytes not in added:
            added.add(control_bytes)
            handlers.append(cls._ValueHandler(controls, fail_enum,
                header_proto))
    return handlers
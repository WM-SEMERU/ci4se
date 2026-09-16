def get_trace_name(object):
    global TRACE_NAMES_CACHE
    global TRACE_WALKER_CACHE
    trace_name = TRACE_NAMES_CACHE.get(object)
    if trace_name is None:
        TRACE_NAMES_CACHE[object] = trace_name = get_object_name(object)
        if type(object) is property:
            object = object.fget
        module = inspect.getmodule(object)
        if module is None:
            return
        members = TRACE_WALKER_CACHE.get(module)
        if members is None:
            TRACE_WALKER_CACHE[module] = members = tuple(trace_walker(module))
        for cls, member in members:
            if object in (cls, untracer(member)):
                TRACE_NAMES_CACHE[object] = trace_name = '.'.join(map(
                    get_object_name, filter(lambda x: x is not None, (
                    module, cls, member))))
                break
    return trace_name
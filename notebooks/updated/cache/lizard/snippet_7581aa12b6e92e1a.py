def retrieve_prop(name):
    handler_get, handler_set = None, None
    if name in props_get:
        handler_get = props_get[name]
    if name in props_set:
        handler_set = props_set[name]
    return name, handler_get, handler_set
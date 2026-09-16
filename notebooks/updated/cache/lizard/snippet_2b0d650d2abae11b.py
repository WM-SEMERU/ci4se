def inplace_reload(method):

    def wrapped(obj, *args, **kwargs):
        in_place = True if kwargs.get('inplace') in (True, None) else False
        api_object = method(obj, *args, **kwargs)
        if in_place and api_object:
            obj._data = api_object._data
            obj._dirty = api_object._dirty
            obj._data.fetched = False
            return obj
        elif api_object:
            return api_object
        else:
            return obj
    return wrapped
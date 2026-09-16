def add_to_obj(obj, dictionary, objs=None, exceptions=None, verbose=0):
    if exceptions is None:
        exceptions = []
    for item in dictionary:
        if item in exceptions:
            continue
        if dictionary[item] is not None:
            if verbose:
                print('process: ', item, dictionary[item])
            key, value = get_key_value(dictionary[item], objs, key=item)
            if verbose:
                print('assign: ', key, value)
            try:
                setattr(obj, key, value)
            except AttributeError:
                raise AttributeError("Can't set {0}={1} on object: {2}".
                    format(key, value, obj))
def set_mixin(target, resource, name=None, override=True):
    if name is None and not hasattr(resource, '__name__'):
        raise Mixin.MixInError(
            "name must be given or resource {0} can't be anonymous".format(
            resource))
    result = None
    name = resource.__name__ if name is None else name
    mixedins_by_name = Mixin.get_mixedins_by_name(target)
    result = getattr(target, name, Mixin.__NEW_CONTENT_KEY__)
    if override or result == Mixin.__NEW_CONTENT_KEY__:
        if name not in mixedins_by_name:
            mixedins_by_name[name] = result,
        else:
            mixedins_by_name[name] += result,
        try:
            setattr(target, name, resource)
        except (AttributeError, TypeError):
            if len(mixedins_by_name[name]) == 1:
                del mixedins_by_name[name]
                if len(mixedins_by_name) == 0:
                    delattr(target, Mixin.__MIXEDIN_KEY__)
            else:
                mixedins_by_name[name] = mixedins_by_name[name][:-2]
            result = None
    else:
        result = None
    return result
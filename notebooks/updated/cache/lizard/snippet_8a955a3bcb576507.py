def remove_mixin(target, name, mixedin=None, replace=True):
    try:
        result = getattr(target, name)
    except AttributeError:
        raise Mixin.MixInError('No mixin {0} exists in {1}'.format(name,
            target))
    mixedins_by_name = Mixin.get_mixedins_by_name(target)
    mixedins = mixedins_by_name.get(name)
    if mixedins:
        if mixedin is None:
            mixedin = mixedins[-1]
            mixedins = mixedins[:-2]
        else:
            try:
                index = mixedins.index(mixedin)
            except ValueError:
                raise Mixin.MixInError(
                    'Mixedin {0} with name {1} does not exist                         in target {2}'
                    .format(mixedin, name, target))
            mixedins = mixedins[0:index] + mixedins[index + 1:]
        if len(mixedins) == 0:
            if mixedin != Mixin.__NEW_CONTENT_KEY__:
                setattr(target, name, mixedin)
            else:
                delattr(target, name)
            del mixedins_by_name[name]
        else:
            if replace:
                setattr(target, name, mixedin)
            mixedins_by_name[name] = mixedins
    else:
        raise Mixin.MixInError('No mixin {0} exists in {1}'.format(name,
            target))
    if len(mixedins_by_name) == 0:
        delattr(target, Mixin.__MIXEDIN_KEY__)
    return result
def booted(context=None):
    contextkey = 'salt.utils.systemd.booted'
    if isinstance(context, dict):
        if contextkey in context:
            return context[contextkey]
    elif context is not None:
        raise SaltInvocationError('context must be a dictionary if passed')
    try:
        ret = bool(os.stat('/run/systemd/system'))
    except OSError:
        ret = False
    try:
        context[contextkey] = ret
    except TypeError:
        pass
    return ret
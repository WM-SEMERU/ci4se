def get_class_alias(klass):
    for k, v in pyamf.ALIAS_TYPES.iteritems():
        for kl in v:
            try:
                if issubclass(klass, kl):
                    return k
            except TypeError:
                if hasattr(kl, '__call__'):
                    if kl(klass) is True:
                        return k
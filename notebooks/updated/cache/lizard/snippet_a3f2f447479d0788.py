def get(cls, *args, **kwargs):
    if len(args) == 1:
        pk = args[0]
    elif kwargs:
        if len(kwargs) == 1 and cls._field_is_pk(list(kwargs.keys())[0]):
            pk = list(kwargs.values())[0]
        else:
            result = cls.collection(**kwargs).sort(by='nosort')
            if len(result) == 0:
                raise DoesNotExist('No object matching filter: %s' % kwargs)
            elif len(result) > 1:
                raise ValueError('More than one object matching filter: %s' %
                    kwargs)
            else:
                try:
                    pk = result[0]
                except IndexError:
                    raise DoesNotExist('No object matching filter: %s' % kwargs
                        )
    else:
        raise ValueError('Invalid `get` usage with args %s and kwargs %s' %
            (args, kwargs))
    return cls(pk)
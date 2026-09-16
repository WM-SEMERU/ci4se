def get(cls, **kwargs):
    things = cls.filter(**kwargs)
    if len(things) > 1:
        raise cls.MultipleObjectsReturned
    elif len(things) == 0:
        raise cls.DoesNotExist
    return things[0]
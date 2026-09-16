def getStat(cls, obj, name):
    objClass = type(obj)
    for theClass in objClass.__mro__:
        if theClass == object:
            break
        for value in theClass.__dict__.values():
            if isinstance(value, Stat) and value.getName() == name:
                return value
def ismethoddescriptor(object):
    return hasattr(object, '__get__') and not hasattr(object, '__set__'
        ) and not ismethod(object) and not isfunction(object) and not isclass(
        object)
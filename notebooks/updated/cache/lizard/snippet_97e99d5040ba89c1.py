def tupleize(element, ignore_types=(str, bytes)):
    if hasattr(element, '__iter__') and not isinstance(element, ignore_types):
        return element
    else:
        return tuple((element,))
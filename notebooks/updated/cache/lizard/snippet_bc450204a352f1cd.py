def getattr_in(obj, name):
    for part in name.split('.'):
        obj = getattr(obj, part)
    return obj
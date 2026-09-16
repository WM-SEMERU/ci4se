def dug(obj, key, value):
    array = key.split('.')
    return _dug(obj, value, *array)
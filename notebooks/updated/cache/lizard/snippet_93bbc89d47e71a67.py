def get_tuple(self):
    objType, objInstance = self.value
    if isinstance(objType, int):
        pass
    elif isinstance(objType, long):
        objType = int(objType)
    elif isinstance(objType, basestring):
        objType = self.objectTypeClass()[objType]
    else:
        raise TypeError('invalid datatype for objType')
    return objType, objInstance
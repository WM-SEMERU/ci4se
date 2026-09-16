def GetUcsMethodMeta(classId, key):
    if classId in _MethodFactoryMeta:
        if key in _MethodFactoryMeta[classId]:
            return _MethodFactoryMeta[classId][key]
    return None
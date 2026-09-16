def FindClassIdInMethodMetaIgnoreCase(classId):
    if classId in _MethodFactoryMeta:
        return classId
    lClassId = classId.lower()
    for key in _MethodFactoryMeta.keys():
        if key.lower() == classId.lower():
            return key
    return None
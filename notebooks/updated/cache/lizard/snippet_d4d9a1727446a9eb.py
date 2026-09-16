def transformToNative(obj):
    if obj.isNative:
        return obj
    obj.isNative = True
    if obj.value == '':
        obj.value = []
        return obj
    tzinfo = getTzid(getattr(obj, 'tzid_param', None))
    obj.value = [stringToPeriod(x, tzinfo) for x in obj.value.split(',')]
    return obj
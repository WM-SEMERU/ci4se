def transformFromNative(cls, obj):
    if obj.isNative:
        obj.isNative = False
        tzid = TimezoneComponent.registerTzinfo(obj.value.tzinfo)
        obj.value = dateTimeToString(obj.value, cls.forceUTC)
        if not cls.forceUTC and tzid is not None:
            obj.tzid_param = tzid
        if obj.params.get('X-VOBJ-ORIGINAL-TZID'):
            if not hasattr(obj, 'tzid_param'):
                obj.tzid_param = obj.x_vobj_original_tzid_param
            del obj.params['X-VOBJ-ORIGINAL-TZID']
    return obj
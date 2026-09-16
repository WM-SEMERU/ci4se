def check_permission(permission, brain_or_object):
    sm = get_security_manager()
    obj = api.get_object(brain_or_object)
    return sm.checkPermission(permission, obj) == 1
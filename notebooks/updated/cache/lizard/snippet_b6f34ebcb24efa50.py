def check_permission(permission, obj):
    mtool = api.get_tool('portal_membership')
    object = api.get_object(obj)
    return mtool.checkPermission(permission, object)
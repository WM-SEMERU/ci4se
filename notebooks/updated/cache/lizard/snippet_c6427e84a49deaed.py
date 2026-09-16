def check_permission(instance, field, permission):
    if not get_permission_test(instance, field, permission)(instance):
        raise PermissionDeniedError(permission, instance, instance, field)
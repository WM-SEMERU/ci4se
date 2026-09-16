def has_permission(user, permission_name):
    if user and user.is_superuser:
        return True
    return permission_name in available_perm_names(user)
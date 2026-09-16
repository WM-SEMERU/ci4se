def get_disallowed_permissions_for(brain_or_object, user=None):
    disallowed = []
    user = get_user(user)
    obj = api.get_object(brain_or_object)
    for permission in get_mapped_permissions_for(brain_or_object):
        if not user.has_permission(permission, obj):
            disallowed.append(permission)
    return disallowed
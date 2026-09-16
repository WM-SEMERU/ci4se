def filer_has_permission(context, item, action):
    permission_method_name = 'has_{action}_permission'.format(action=action)
    permission_method = getattr(item, permission_method_name, None)
    request = context.get('request')
    if not permission_method or not request:
        return False
    return permission_method(request)
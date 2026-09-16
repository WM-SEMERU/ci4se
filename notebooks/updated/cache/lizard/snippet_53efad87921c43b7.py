def get_users_with_permission(obj, permission):
    user_model = get_user_model()
    return user_model.objects.filter(userobjectpermission__object_pk=obj.pk,
        userobjectpermission__permission__codename=permission).distinct()
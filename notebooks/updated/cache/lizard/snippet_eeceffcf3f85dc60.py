def check_permissions(self):
    changed_permissions = []
    changed_users = []
    warnings = []
    for model, perms in ASSIGNED_PERMISSIONS.items():
        if model == 'profile':
            model_obj = get_profile_model()
        else:
            model_obj = get_user_model()
        model_content_type = ContentType.objects.get_for_model(model_obj)
        for perm in perms:
            try:
                Permission.objects.get(codename=perm[0], content_type=
                    model_content_type)
            except Permission.DoesNotExist:
                changed_permissions.append(perm[1])
                Permission.objects.create(name=perm[1], codename=perm[0],
                    content_type=model_content_type)
    for user in get_user_model().objects.exclude(username=settings.
        ANONYMOUS_USER_NAME):
        try:
            user_profile = get_user_profile(user=user)
        except ObjectDoesNotExist:
            warnings.append(_('No profile found for %(username)s') % {
                'username': user.username})
        else:
            all_permissions = get_perms(user, user_profile) + get_perms(user,
                user)
            for model, perms in ASSIGNED_PERMISSIONS.items():
                if model == 'profile':
                    perm_object = get_user_profile(user=user)
                else:
                    perm_object = user
                for perm in perms:
                    if perm[0] not in all_permissions:
                        assign_perm(perm[0], user, perm_object)
                        changed_users.append(user)
    return changed_permissions, changed_users, warnings
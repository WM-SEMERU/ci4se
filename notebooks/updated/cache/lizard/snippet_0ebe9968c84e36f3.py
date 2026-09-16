def grant_permissions(self, proxy_model):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    try:
        Permission = apps.get_model('auth', 'Permission')
    except LookupError:
        return
    searched_perms = []
    ctype = ContentType.objects.get_for_model(proxy_model)
    for perm in self.default_permissions:
        searched_perms.append(('{0}_{1}'.format(perm, proxy_model._meta.
            model_name), 'Can {0} {1}'.format(perm, proxy_model._meta.
            verbose_name_raw)))
    all_perms = set(Permission.objects.filter(content_type=ctype).
        values_list('content_type', 'codename'))
    permissions = [Permission(codename=codename, name=name, content_type=
        ctype) for codename, name in searched_perms if (ctype.pk, codename)
         not in all_perms]
    Permission.objects.bulk_create(permissions)
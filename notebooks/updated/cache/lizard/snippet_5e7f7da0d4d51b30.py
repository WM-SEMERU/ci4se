def has_object_permission(self, request, view, obj):
    if request.user.is_superuser:
        return True
    if 'permissions' in view.action:
        self.perms_map['POST'] = ['%(app_label)s.share_%(model_name)s']
    if view.action in ['add_data', 'remove_data']:
        self.perms_map['POST'] = ['%(app_label)s.add_%(model_name)s']
    if hasattr(view, 'get_queryset'):
        queryset = view.get_queryset()
    else:
        queryset = getattr(view, 'queryset', None)
    assert queryset is not None, 'Cannot apply DjangoObjectPermissions on a view that does not set `.queryset` or have a `.get_queryset()` method.'
    model_cls = queryset.model
    user = request.user
    perms = self.get_required_object_permissions(request.method, model_cls)
    if not user.has_perms(perms, obj) and not AnonymousUser().has_perms(perms,
        obj):
        if request.method in permissions.SAFE_METHODS:
            raise Http404
        read_perms = self.get_required_object_permissions('GET', model_cls)
        if not user.has_perms(read_perms, obj):
            raise Http404
        return False
    return True
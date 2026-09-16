def has_edit_permission(self, request, obj=None, version=None):
    permission_name = '{}.edit_{}'.format(self.opts.app_label, self.opts.
        model_name)
    has_permission = request.user.has_perm(permission_name)
    if obj is not None and has_permission is False:
        has_permission = request.user.has_perm(permission_name, obj=obj)
    if has_permission and version is not None:
        if version.version_number or version.owner != request.user:
            has_permission = False
    return has_permission
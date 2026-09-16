def has_delete_permission(self, request, obj=None):
    if obj is not None and obj.fixed:
        return False
    return super(NamespaceAdmin, self).has_delete_permission(request, obj)
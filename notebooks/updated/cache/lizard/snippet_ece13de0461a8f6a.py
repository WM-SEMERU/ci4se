def check_permission(self, request, page, permission):
    if not getattr(page, 'can_' + permission)(request):
        raise PermissionDenied
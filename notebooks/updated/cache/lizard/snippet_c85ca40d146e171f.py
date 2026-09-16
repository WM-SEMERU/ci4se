def _view(self, request, extra_context=None):
    if not self.has_permission(request.user):
        raise PermissionDenied
    return self.view(request, self.construct_context(request))
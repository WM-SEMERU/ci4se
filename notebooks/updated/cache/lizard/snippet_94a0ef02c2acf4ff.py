def DeletePermission(self, permission_link, options=None):
    if options is None:
        options = {}
    path = base.GetPathFromLink(permission_link)
    permission_id = base.GetResourceIdOrFullNameFromLink(permission_link)
    return self.DeleteResource(path, 'permissions', permission_id, None,
        options)
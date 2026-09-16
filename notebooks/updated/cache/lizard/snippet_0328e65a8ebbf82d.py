def DeleteUser(self, user_link, options=None):
    if options is None:
        options = {}
    path = base.GetPathFromLink(user_link)
    user_id = base.GetResourceIdOrFullNameFromLink(user_link)
    return self.DeleteResource(path, 'users', user_id, None, options)
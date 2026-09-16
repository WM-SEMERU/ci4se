def perform_permissions_check(self, user, obj, perms):
    checker = self.request.forum_permission_handler._get_checker(user)
    return all(checker.has_perm(perm, obj) for perm in perms)
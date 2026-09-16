def _perform_basic_permission_check(self, forum, user, permission):
    checker = self._get_checker(user)
    check = user.is_superuser or checker.has_perm(permission, forum)
    return check
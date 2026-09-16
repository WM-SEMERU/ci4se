def check_perms(perms, user, slug, raise_exception=False):
    if isinstance(perms, string_types):
        perms = {perms}
    else:
        perms = set(perms)
    allowed_users = ACLRule.get_users_for(perms, slug)
    if allowed_users:
        return user in allowed_users
    if perms.issubset(set(WALIKI_ANONYMOUS_USER_PERMISSIONS)):
        return True
    if is_authenticated(user) and perms.issubset(set(
        WALIKI_LOGGED_USER_PERMISSIONS)):
        return True
    if user.has_perms([('waliki.%s' % p) for p in perms]):
        return True
    if raise_exception:
        raise PermissionDenied
    return False
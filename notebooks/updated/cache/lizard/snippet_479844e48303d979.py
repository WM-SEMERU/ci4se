def get_groups(user=None):
    portal_groups = get_tool('portal_groups')
    user = get_user(user)
    if user is None:
        return []
    return portal_groups.getGroupsForPrincipal(user)
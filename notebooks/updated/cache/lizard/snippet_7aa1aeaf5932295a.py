def check_read_permission(self, user_id, do_raise=True):
    if _is_admin(user_id):
        return True
    if int(self.created_by) == int(user_id):
        return True
    for owner in self.owners:
        if int(owner.user_id) == int(user_id):
            if owner.view == 'Y':
                break
    else:
        if do_raise is True:
            raise PermissionError(
                'Permission denied. User %s does not have read access on network %s'
                 % (user_id, self.id))
        else:
            return False
    return True
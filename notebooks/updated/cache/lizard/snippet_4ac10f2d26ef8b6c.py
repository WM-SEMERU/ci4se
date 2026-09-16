def is_analyst_assignment_allowed(self):
    if not self.allow_edit:
        return False
    if not self.can_manage:
        return False
    if self.filter_by_user:
        return False
    return True
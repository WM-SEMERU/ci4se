def can_user_approve_this_page(self, user):
    self.ensure_one()
    if not self.is_approval_required:
        return True
    if user.has_group('document_page.group_document_manager'):
        return True
    if not user.has_group('document_page_approval.group_document_approver_user'
        ):
        return False
    if not self.approver_group_ids:
        return True
    return len(user.groups_id & self.approver_group_ids) > 0
def user_can_add_attachments(self):
    if not self.global_attachments_allowed():
        return False
    context = self.context
    pm = api.get_tool('portal_membership')
    return pm.checkPermission(AddAttachment, context)
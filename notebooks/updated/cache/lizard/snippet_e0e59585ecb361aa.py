def update(self):
    super(AttachmentsViewlet, self).update()
    self.attachments_view = self.get_attachments_view()
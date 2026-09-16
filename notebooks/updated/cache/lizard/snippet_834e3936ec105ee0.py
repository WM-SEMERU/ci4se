def ReadAttachment(self, attachment_link, options=None):
    if options is None:
        options = {}
    path = base.GetPathFromLink(attachment_link)
    attachment_id = base.GetResourceIdOrFullNameFromLink(attachment_link)
    return self.Read(path, 'attachments', attachment_id, None, options)
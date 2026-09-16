def UpsertAttachment(self, document_link, attachment, options=None):
    if options is None:
        options = {}
    document_id, path = self._GetItemIdWithPathForAttachment(attachment,
        document_link)
    return self.Upsert(attachment, path, 'attachments', document_id, None,
        options)
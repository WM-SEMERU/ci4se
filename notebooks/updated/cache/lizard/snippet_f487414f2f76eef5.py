def CreateAttachmentAndUploadMedia(self, document_link, readable_stream,
    options=None):
    if options is None:
        options = {}
    document_id, initial_headers, path = (self.
        _GetItemIdWithPathForAttachmentMedia(document_link, options))
    return self.Create(readable_stream, path, 'attachments', document_id,
        initial_headers, options)
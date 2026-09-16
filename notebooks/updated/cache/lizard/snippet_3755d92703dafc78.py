def bulk_attachments(self, article, attachments):
    return HelpdeskAttachmentRequest(self).post(self.endpoint.
        bulk_attachments, article=article, attachments=attachments)
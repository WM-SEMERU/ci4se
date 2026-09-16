def delete_attachment(cls, session, attachment):
    return super(Conversations, cls).delete(session, attachment,
        endpoint_override='/attachments/%s.json' % attachment.id, out_type=
        Attachment)
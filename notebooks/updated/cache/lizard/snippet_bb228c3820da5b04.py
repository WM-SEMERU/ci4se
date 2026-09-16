def get_attachment_data(cls, session, attachment_id):
    return cls('/attachments/%d/data.json' % attachment_id, singleton=True,
        session=session, out_type=AttachmentData)
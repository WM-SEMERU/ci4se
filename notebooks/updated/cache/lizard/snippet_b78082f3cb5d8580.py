def to_email_attachment(self, filename, filedata, **kw):
    maintype = 'application'
    subtype = 'octet-stream'
    mime_type = mimetypes.guess_type(filename)[0]
    if mime_type is not None:
        maintype, subtype = mime_type.split('/')
    attachment = MIMEBase(maintype, subtype, **kw)
    attachment.set_payload(filedata)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename=%s' %
        filename)
    return attachment
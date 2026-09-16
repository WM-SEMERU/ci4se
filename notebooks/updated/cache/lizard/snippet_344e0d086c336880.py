def create_attachments(attachment_files):
    attachments = []
    for filename, filedata in attachment_files.items():
        if isinstance(filedata, dict):
            content = filedata.get('file', None)
            mimetype = filedata.get('mimetype', None)
            headers = filedata.get('headers', None)
        else:
            content = filedata
            mimetype = None
            headers = None
        opened_file = None
        if isinstance(content, string_types):
            opened_file = open(content, 'rb')
            content = File(opened_file)
        attachment = Attachment()
        if mimetype:
            attachment.mimetype = mimetype
        attachment.headers = headers
        attachment.file.save(filename, content=content, save=True)
        attachments.append(attachment)
        if opened_file is not None:
            opened_file.close()
    return attachments
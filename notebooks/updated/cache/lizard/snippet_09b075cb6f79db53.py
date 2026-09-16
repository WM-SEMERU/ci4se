def get_attachment_data(self, attachment):
    f = attachment.getAttachmentFile()
    attachment_type = attachment.getAttachmentType()
    attachment_keys = attachment.getAttachmentKeys()
    filename = f.filename
    filesize = self.get_filesize(f)
    mimetype = f.getContentType()
    report_option = attachment.getReportOption()
    return {'obj': attachment, 'attachment_type': attachment_type,
        'attachment_keys': attachment_keys, 'file': f, 'uid': api.get_uid(
        attachment), 'filesize': filesize, 'filename': filename, 'mimetype':
        mimetype, 'report_option': report_option}
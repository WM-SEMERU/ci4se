def get_attachment_size(self, attachment):
    fsize = 0
    file = attachment.getAttachmentFile()
    if file:
        fsize = file.get_size()
    if fsize < 1024:
        fsize = '%s b' % fsize
    else:
        fsize = '%s Kb' % (fsize / 1024)
    return fsize
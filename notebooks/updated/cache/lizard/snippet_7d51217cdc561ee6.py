def GetAttachmentIdFromMediaId(media_id):
    altchars = '+-'
    if not six.PY2:
        altchars = altchars.encode('utf-8')
    buffer = base64.b64decode(str(media_id), altchars)
    resoure_id_length = 20
    attachment_id = ''
    if len(buffer) > resoure_id_length:
        attachment_id = base64.b64encode(buffer[0:resoure_id_length], altchars)
        if not six.PY2:
            attachment_id = attachment_id.decode('utf-8')
    else:
        attachment_id = media_id
    return attachment_id
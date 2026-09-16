def getFileDialogTitle(msg, title):
    if msg and title:
        return '%s - %s' % (title, msg)
    if msg and not title:
        return str(msg)
    if title and not msg:
        return str(title)
    return None
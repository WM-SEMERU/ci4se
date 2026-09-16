def lookup_dirent(event, filesystem_content, journal_content):
    for dirent in filesystem_content[event.inode]:
        if dirent.path.endswith(event.name):
            return dirent
    path = lookup_folder(event, filesystem_content)
    if path is not None:
        return Dirent(event.inode, path, -1, None, False, 0, 0, 0, 0)
    path = lookup_deleted_folder(event, filesystem_content, journal_content)
    if path is not None:
        return Dirent(event.inode, path, -1, None, False, 0, 0, 0, 0)
    raise LookupError('File %s not found' % event.name)
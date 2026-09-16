def convert_errno(e):
    if e == errno.EACCES:
        return SFTP_PERMISSION_DENIED
    elif e == errno.ENOENT or e == errno.ENOTDIR:
        return SFTP_NO_SUCH_FILE
    else:
        return SFTP_FAILURE
def user_owns_file(path, uid=None):
    if uid is None:
        uid = os.getuid()
    path = os.path.expandvars(os.path.expanduser(path))
    return os.stat(path).st_uid == uid
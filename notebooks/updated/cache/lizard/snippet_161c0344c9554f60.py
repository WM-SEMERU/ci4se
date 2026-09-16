def get_user(path, follow_symlinks=True):
    if not os.path.exists(path):
        raise CommandExecutionError('Path not found: {0}'.format(path))
    if follow_symlinks and sys.getwindowsversion().major >= 6:
        path = _resolve_symlink(path)
    return salt.utils.win_dacl.get_owner(path)
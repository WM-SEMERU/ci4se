def symlink(src, link):
    if sys.getwindowsversion().major < 6:
        raise SaltInvocationError(
            'Symlinks are only supported on Windows Vista or later.')
    if not os.path.exists(src):
        raise SaltInvocationError('The given source path does not exist.')
    if not os.path.isabs(src):
        raise SaltInvocationError('File path must be absolute.')
    src = os.path.normpath(src)
    link = os.path.normpath(link)
    is_dir = os.path.isdir(src)
    try:
        win32file.CreateSymbolicLink(link, src, int(is_dir))
        return True
    except pywinerror as exc:
        raise CommandExecutionError("Could not create '{0}' - [{1}] {2}".
            format(link, exc.winerror, exc.strerror))
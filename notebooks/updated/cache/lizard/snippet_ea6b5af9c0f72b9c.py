def utime(self, tarinfo, targetpath):
    if not hasattr(os, 'utime'):
        return
    try:
        os.utime(targetpath, (tarinfo.mtime, tarinfo.mtime))
    except EnvironmentError as e:
        raise ExtractError('could not change modification time')
def _relpath(name):
    return os.path.normpath(os.path.splitdrive(name)[1]).lstrip(_allsep)
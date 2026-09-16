def _is_link(fs, path):
    try:
        return stat.S_ISLNK(fs.lstat(path).st_mode)
    except exceptions.FileNotFound:
        return False
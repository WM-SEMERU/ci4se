def expanduser(path):
    if hdfs_fs.default_is_local():
        return os.path.expanduser(path)
    m = re.match('^~([^/]*)', path)
    if m is None:
        return path
    user = m.groups()[0] or common.DEFAULT_USER
    return '/user/%s%s' % (user, path[m.end(1):])
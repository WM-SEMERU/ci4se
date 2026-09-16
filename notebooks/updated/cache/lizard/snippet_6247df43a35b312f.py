def CheckPathExists(path):
    i = 0
    root, ext = os.path.splitext(path)
    while os.path.exists(path):
        i = i + 1
        goodlogging.Log.Info('UTIL', 'Path {0} already exists'.format(path))
        path = '{0}_{1}'.format(root, i) + ext
    return path
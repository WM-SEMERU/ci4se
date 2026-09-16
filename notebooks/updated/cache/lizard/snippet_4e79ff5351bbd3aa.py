def path_from_pythonpath(pythonpath):
    path = fs.Path()
    for p in pythonpath.split(os.pathsep):
        path.add_path(utils.expand_path(p), 'os')
    return path
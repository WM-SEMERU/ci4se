def current_git_dir():
    path = os.path.abspath(os.curdir)
    while path != '/':
        if os.path.isdir(os.path.join(path, '.git')):
            return os.path.join(path, '.git')
        path = os.path.dirname(path)
    return None
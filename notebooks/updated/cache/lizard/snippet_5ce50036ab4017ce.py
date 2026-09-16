def get_absolute_path(cls, roots, path):
    for root in roots:
        abspath = os.path.abspath(os.path.join(root, path))
        if abspath.startswith(root) and os.path.exists(abspath):
            return abspath
    return 'file-not-found'
def reverse(path):
    if is_rooted(path) or '..' in path:
        from b2.manager import get_manager
        get_manager().errors()(
            'reverse(path): path is either rooted or contains ".." in the path'
            )
    if path == '.':
        return path
    path = os.path.normpath(path)
    return os.sep.join('..' for t in path.split(os.sep))
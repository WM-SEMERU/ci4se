def compare_recursive_mtime(path, cutoff, newest=True):
    if os.path.isfile(path):
        mt = mtime(path)
        if newest:
            if mt > cutoff:
                return True
        elif mt < cutoff:
            return True
    for dirname, _, filenames in os.walk(path, topdown=False):
        for filename in filenames:
            mt = mtime(os.path.join(dirname, filename))
            if newest:
                if mt > cutoff:
                    return True
            elif mt < cutoff:
                return True
    return False
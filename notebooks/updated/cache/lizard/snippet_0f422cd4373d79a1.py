def match_file(filename, exclude):
    base_name = os.path.basename(filename)
    if base_name.startswith('.'):
        return False
    for pattern in exclude:
        if fnmatch.fnmatch(base_name, pattern):
            return False
        if fnmatch.fnmatch(filename, pattern):
            return False
    if not os.path.isdir(filename) and not is_python_file(filename):
        return False
    return True
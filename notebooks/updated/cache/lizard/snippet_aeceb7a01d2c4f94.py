def absolute_path(path, from_file):
    if path is None:
        return None
    current_directory = os.path.dirname(from_file)
    target = os.path.join(current_directory, path)
    return os.path.abspath(target)
def ensure_parent_directory(path, ensure_parent=True):
    parent_directory = os.path.abspath(path)
    if ensure_parent:
        parent_directory = os.path.dirname(parent_directory)
    if not os.path.exists(parent_directory):
        try:
            os.makedirs(parent_directory)
        except (IOError, OSError):
            raise OSError("Directory '%s' cannot be created" % parent_directory
                )
def is_executable(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)
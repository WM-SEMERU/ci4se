def resolve_path(path, config_file):
    if os.path.isabs(path):
        return path
    return os.path.relpath(path, os.path.dirname(config_file))
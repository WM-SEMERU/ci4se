def parent_folder(path, base=None):
    return path and os.path.dirname(resolved_path(path, base=base))
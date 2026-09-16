def _resolve_file(file_name):
    if not file_name:
        return None
    path = os.path.realpath(file_name)
    if os.path.isfile(path):
        return path
    return None
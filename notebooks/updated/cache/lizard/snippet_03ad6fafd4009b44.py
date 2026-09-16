def _ensure_directory_exists(self, directory):
    if not os.path.lexists(directory):
        os.makedirs(directory)
    return directory